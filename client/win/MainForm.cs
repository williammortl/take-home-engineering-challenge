// --------------------------------------------------------------------------------------------------------------------
// <copyright file="MainForm.cs" company="Microsoft">
//   2018 William M Mortl
// </copyright>
// --------------------------------------------------------------------------------------------------------------------

namespace FoodTruck
{
    using FoodTruck.FoodtruckServiceInterop;
    using Newtonsoft.Json;
    using Newtonsoft.Json.Linq;
    using System;
    using System.Configuration;
    using System.IO;
    using System.Net;
    using System.Text;
    using System.Windows.Forms;

    /// <summary>
    /// Main form class
    /// </summary>
    public partial class MainForm : Form
    {
        private const string GoogleURL = "https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}";
        private const string GoogleFormatAddress = "{0},{1},{2}";

        private string googleAPIKey;
        private string foodtruckURL;
        private string foodtruckAPIKey;

        /// <summary>
        /// Constructor
        /// </summary>
        public MainForm()
        {
            InitializeComponent();
            this.googleAPIKey = ConfigurationManager.AppSettings["GoogleAPIKey"];
            this.foodtruckURL = ConfigurationManager.AppSettings["FoodtruckURL"];
            this.foodtruckAPIKey = ConfigurationManager.AppSettings["FoodtruckAPIKey"];
        }

        /// <summary>
        /// Form load
        /// </summary>
        /// <param name="sender">who triggered</param>
        /// <param name="e">event args</param>
        private void MainForm_Load(object sender, EventArgs e)
        {
            this.Location = new System.Drawing.Point(0, 0);
        }

        /// <summary>
        /// Search for foodtrucks
        /// </summary>
        /// <param name="sender">who triggered</param>
        /// <param name="e">event args</param>
        private void GoButton_Click(object sender, EventArgs e)
        {
            this.GoButton.Enabled = false;
            this.Cursor = Cursors.WaitCursor;

            // resolve address to lat and long
            var latAndLong = CallGoogleApi();
            this.Latitude.Text = latAndLong.Item1.ToString();
            this.Longitude.Text = latAndLong.Item2.ToString();

            // call food truck service
            this.FoodtruckList.Text = this.CallFoodtruckService(
                latAndLong.Item1,
                latAndLong.Item2);

            this.Cursor = Cursors.Default;
            this.GoButton.Enabled = true;
        }

        /// <summary>
        /// Call foodtruck service and 
        /// </summary>
        /// <param name="lat">latitude</param>
        /// <param name="lng">longitude</param>
        /// <returns>string of food trucks</returns>
        private string CallFoodtruckService(double lat, double lng)
        {
            var retVal = string.Empty;
            try
            {

                // format the posted json data
                var postData = JsonConvert.SerializeObject(new FoodtruckRequest() { Latitude = lat, Longitude = lng });
                var byteArray = Encoding.UTF8.GetBytes(postData);

                // prepare the request
                var request = (HttpWebRequest)WebRequest.Create(this.foodtruckURL);
                request.ContentType = "application/json";
                request.Headers.Add("x-api-key", this.foodtruckAPIKey);
                request.Method = "POST";
                request.ContentLength = byteArray.Length;
                var dataStream = request.GetRequestStream();
                dataStream.Write(byteArray, 0, byteArray.Length);
                dataStream.Close();

                // call the service
                var response = request.GetResponse();
                var json = string.Empty;
                using (Stream responseStream = response.GetResponseStream())
                {
                    using (StreamReader reader = new StreamReader(responseStream, System.Text.Encoding.UTF8))
                    {
                        json = reader.ReadToEnd();
                    }
                }

                // parse the JSON
                var foodtrucksResponse = JsonConvert.DeserializeObject<FoodtrucksResponse>(json);
                retVal = this.GenerateFoodtruckReport(foodtrucksResponse);
            }
            catch
            {
                MessageBox.Show("An error occurred while searching for food trucks, please contact support", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                retVal = string.Empty;
            }

            return retVal;
        }

        /// <summary>
        /// Generates human readable report
        /// </summary>
        /// <param name="fr">a food truck response object</param>
        /// <returns>formatted string data</returns>
        private string GenerateFoodtruckReport(FoodtrucksResponse fr)
        {
            StringBuilder sb = new StringBuilder();
            foreach (var f in fr.Foodtrucks)
            {
                sb.Append(string.Format("Name: {0}\r\n", f.Name));
                sb.Append(string.Format("Address: {0}\r\n", f.Address));
                sb.Append(string.Format("Hours: {0}\r\n", f.Hours));
                sb.Append(string.Format("Latitude: {0}\r\n", f.Latitude.ToString()));
                sb.Append(string.Format("Longitude: {0}\r\n", f.Longitude.ToString()));
                sb.Append(string.Format("Menu:\r\n{0}\r\n", f.Menu));
                sb.Append(string.Format("\r\n{0}\r\n\r\n", new string('-', 50)));
            }
            return sb.ToString();
        }

        /// <summary>
        /// Call Google Maps API and resolve address to lat and long
        /// </summary>
        /// <returns>tuple of lat and long</returns>
        private Tuple<double, double> CallGoogleApi()
        {
            var retVal = new Tuple<double, double>(0, 0);
            try
            {

                // build the GET query string
                var address = this.Address.Text.Replace(' ', '+');
                var city = this.City.Text.Replace(' ', '+');
                var state = this.State.Text;
                var completeAddress = string.Format(MainForm.GoogleFormatAddress, address, city, state);
                var completeURL = string.Format(MainForm.GoogleURL, completeAddress, this.googleAPIKey);

                // call the service
                var request = (HttpWebRequest)WebRequest.Create(completeURL);
                var response = request.GetResponse();
                var json = string.Empty;
                using (Stream responseStream = response.GetResponseStream())
                {
                    using (StreamReader reader = new StreamReader(responseStream, System.Text.Encoding.UTF8))
                    {
                        json = reader.ReadToEnd();
                    }
                }

                // parse the JSON
                // NOTE: normally I would deserialize to an object here, but the response is complicated
                //  and due to time constraints I took a shortcut
                var jobject = JObject.Parse(json);
                var latString = jobject["results"][0]["geometry"]["location"]["lat"];
                var lngString = jobject["results"][0]["geometry"]["location"]["lng"];
                retVal = new Tuple<double, double>(Convert.ToDouble(latString), Convert.ToDouble(lngString));
            }
            catch
            {
                MessageBox.Show("An error occurred translating the address to coordinates, please contact support", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                retVal = new Tuple<double, double>(0, 0);
            }

            return retVal;
        }
    }
}
