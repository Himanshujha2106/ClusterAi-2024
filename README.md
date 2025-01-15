
# ClusterAI

ClusterAI is an intelligent tool that groups keywords into meaningful categories using clustering algorithms. It provides users with an efficient way to analyze and organize large datasets of keywords based on their similarity. The web application is built with a combination of frontend, backend, and machine learning technologies.

![ClusterAI Logo](static/images/logo.svg)

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Overview

ClusterAI is an intelligent tool that groups keywords into meaningful categories using clustering algorithms. It provides users with an efficient way to analyze and organize large datasets of keywords based on their similarity. The web application is built with a combination of frontend, backend, and machine learning technologies.

## Features

-**Keyword Upload**: Users can input or upload a list of keywords for analysis.
**Clustering Algorithms**: Implements two clustering methods:
-**K-Means Clustering**: Groups keywords into a predefined number of clusters based on their similarity.
-**Hierarchical Clustering**: Creates a tree-like structure to display the relationships between clusters.
-**Interactive Visualization**: Provides visual representations of the clustered data, such as dendrograms or scatter plots.
-**Export Options**: Allows users to download the clustered results in CSV or JSON format.
-**Simple and Intuitive UI**: Easy-to-use interface for both technical and non-technical users.

## Installation

To set up ClusterAI on your local machine, follow these instructions:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Himanshujha2106/ClusterAi-2024.git
   cd ClusterAi-2024
   ```

2. **Set Up a Virtual Environment:**

   ```bash
   python -m venv clusteraienv
   source clusteraienv/bin/activate  # On Windows: `clusteraienv\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Database Migrations:**

   ```bash
   python manage.py migrate
   ```

5. **Collect Static Files:**

   ```bash
   python manage.py collectstatic
   ```

6. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser to see the application in action.

## Usage

ClusterAI is designed to be intuitive and user-friendly. Here’s how you can start using the platform:

1. **Log In:** Sign up or log in using your credentials.
2. **Upload Data:** Upload datasets via the web interface or API.
3. **Configure Clustering:** Choose your clustering algorithm and configure the parameters.
4. **Visualize Results:** Generate interactive visualizations to explore the clustered data.
5. **Export Results:** Download the clustered data and visualizations for further analysis.

## Configuration

ClusterAI can be customized to fit your needs. Here are some of the configurations you can tweak:

- **Settings:** Modify `settings.py` to configure database connections, debug options, and more.
- **Environment Variables:** Use a `.env` file to manage sensitive information such as API keys and database credentials.
- **Custom Pipelines:** Extend or modify the data processing pipelines by editing the relevant modules in the project.

## Contributing

We welcome contributions from the community! To contribute to ClusterAI, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

Please refer to `CONTRIBUTING.md` for more detailed guidelines.

## License

ClusterAI is licensed under the MIT License. See the `LICENSE` file for more information.

## Contact

If you have any questions or need further assistance, feel free to reach out:

- Email: [himanshujha2106@gmail.com](mailto:himanshujha2106@gmail.com)
- GitHub: [Himanshujha2106](https://github.com/Himanshujha2106)

Thank you for using ClusterAI!
