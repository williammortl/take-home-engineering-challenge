namespace FoodTruck
{
    partial class MainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainForm));
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.Latitude = new System.Windows.Forms.TextBox();
            this.Longitude = new System.Windows.Forms.TextBox();
            this.FoodtruckList = new System.Windows.Forms.TextBox();
            this.GoButton = new System.Windows.Forms.Button();
            this.Address = new System.Windows.Forms.TextBox();
            this.City = new System.Windows.Forms.TextBox();
            this.State = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.label4 = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.SuspendLayout();
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(16, 111);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(71, 20);
            this.label1.TabIndex = 0;
            this.label1.Text = "Latitude:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(16, 140);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(84, 20);
            this.label2.TabIndex = 1;
            this.label2.Text = "Longitude:";
            // 
            // Latitude
            // 
            this.Latitude.Font = new System.Drawing.Font("Microsoft Sans Serif", 8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Latitude.Location = new System.Drawing.Point(103, 105);
            this.Latitude.Name = "Latitude";
            this.Latitude.ReadOnly = true;
            this.Latitude.Size = new System.Drawing.Size(137, 26);
            this.Latitude.TabIndex = 2;
            this.Latitude.TabStop = false;
            // 
            // Longitude
            // 
            this.Longitude.Font = new System.Drawing.Font("Microsoft Sans Serif", 8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Longitude.Location = new System.Drawing.Point(103, 137);
            this.Longitude.Name = "Longitude";
            this.Longitude.ReadOnly = true;
            this.Longitude.Size = new System.Drawing.Size(137, 26);
            this.Longitude.TabIndex = 3;
            this.Longitude.TabStop = false;
            // 
            // FoodtruckList
            // 
            this.FoodtruckList.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.FoodtruckList.Location = new System.Drawing.Point(20, 225);
            this.FoodtruckList.Multiline = true;
            this.FoodtruckList.Name = "FoodtruckList";
            this.FoodtruckList.ReadOnly = true;
            this.FoodtruckList.ScrollBars = System.Windows.Forms.ScrollBars.Vertical;
            this.FoodtruckList.Size = new System.Drawing.Size(763, 690);
            this.FoodtruckList.TabIndex = 4;
            this.FoodtruckList.TabStop = false;
            // 
            // GoButton
            // 
            this.GoButton.BackColor = System.Drawing.Color.Green;
            this.GoButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 16F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.GoButton.ForeColor = System.Drawing.Color.White;
            this.GoButton.Location = new System.Drawing.Point(266, 105);
            this.GoButton.Name = "GoButton";
            this.GoButton.Size = new System.Drawing.Size(517, 95);
            this.GoButton.TabIndex = 3;
            this.GoButton.Text = "Search >>";
            this.GoButton.UseVisualStyleBackColor = false;
            this.GoButton.Click += new System.EventHandler(this.GoButton_Click);
            // 
            // Address
            // 
            this.Address.Location = new System.Drawing.Point(98, 12);
            this.Address.Name = "Address";
            this.Address.Size = new System.Drawing.Size(685, 26);
            this.Address.TabIndex = 0;
            this.Address.Text = "1800 Folsom St";
            // 
            // City
            // 
            this.City.Location = new System.Drawing.Point(98, 57);
            this.City.Name = "City";
            this.City.Size = new System.Drawing.Size(356, 26);
            this.City.TabIndex = 1;
            this.City.Text = "San Francisco";
            // 
            // State
            // 
            this.State.Location = new System.Drawing.Point(558, 57);
            this.State.Name = "State";
            this.State.Size = new System.Drawing.Size(225, 26);
            this.State.TabIndex = 2;
            this.State.Text = "CA";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(16, 15);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(72, 20);
            this.label3.TabIndex = 7;
            this.label3.Text = "Address:";
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(16, 60);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(39, 20);
            this.label4.TabIndex = 8;
            this.label4.Text = "City:";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(490, 60);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(52, 20);
            this.label5.TabIndex = 9;
            this.label5.Text = "State:";
            // 
            // MainForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.ButtonShadow;
            this.ClientSize = new System.Drawing.Size(800, 933);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.State);
            this.Controls.Add(this.City);
            this.Controls.Add(this.Address);
            this.Controls.Add(this.GoButton);
            this.Controls.Add(this.FoodtruckList);
            this.Controls.Add(this.Longitude);
            this.Controls.Add(this.Latitude);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.MaximizeBox = false;
            this.Name = "MainForm";
            this.Text = "Food Truck";
            this.Load += new System.EventHandler(this.MainForm_Load);
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox Latitude;
        private System.Windows.Forms.TextBox Longitude;
        private System.Windows.Forms.TextBox FoodtruckList;
        private System.Windows.Forms.Button GoButton;
        private System.Windows.Forms.TextBox Address;
        private System.Windows.Forms.TextBox City;
        private System.Windows.Forms.TextBox State;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
    }
}

