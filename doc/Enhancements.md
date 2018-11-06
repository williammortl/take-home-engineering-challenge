# Enhancements

Overall there are several enhancements that this service would need to be made prodcution ready:

    1. Implementing additional logic to handle expiring permits
    2. SQLite was chosen due to time constraints, thus migrating from that technology to a more robust technology such as SQL Azure or Mongodb is needed
    3. Implementing a new query for menu items, meaning if you'd like a "hamburger" the service would be able to find the 5 closest hamburger joints
    4. The service needs a "what's open" feature where users are able to filter out food trucks that are currently closed
    5. Obviously this service needs at least a web front end, and most likely iOS and Android mobile apps (which were not done due to time constraints)
    6. More unit tests need to be added for existing as well as new functionality
