# Project Overview

This project was built as a learning exercise to explore Python and Django. It was initially deployed using AWS in a production environment. However, the page has been taken down temporarily to save resources, as there are no meaningful articles available at the moment. In the future, I plan to write and publish articles, after which a static version of the site will be hosted.

## Getting Started

To set up the project, follow the steps below:

1. **Create a `.env` file:**

   Add your `SECRET_KEY` and any other necessary environment variables.

2. **Build the Docker image:**

   Run the following command to build the Docker image:

   ```bash
   docker build -t <your_username>/turazo .

3. **Run the Docker image:**

    Once the image is built, use the command below to run it:

    ```bash
    docker run -d -p 80:80 --env-file .env <your_username>/turazo
