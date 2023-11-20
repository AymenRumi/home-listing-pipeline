# Data Pipeline for Real Estate Analytics


## Project Overview:

This project implements a high-performance Airflow data pipeline for scraping home listings from remax.com. It leverages Selenium for web scraping and employs a multithreaded approach to enhance the scraping speed. The pipeline is designed to scrape pages in parallel using Airflow's Celery Executor backed by Redis, ensuring efficient and scalable data processing.


##  Key Features:
* **Multithreaded Scraping** Utilizes multiple threads to scrape home listings concurrently, significantly speeding up the process.
* **Parallel Processing**: Employs Airflow's Celery Executor with Redis to scrape chunks of pages in parallel.
* **Data Contract**: Implements a data contract using Pydantic for validating scraped data before storage.
* **PostgreSQL Integration**: Stores validated data in a PostgreSQL database.
* **Slowly Changing Dimensions (SCD) Modeling**: Executes a subsequent job to model SCDs in the database.
* **AWS Deployment**: The entire pipeline is deployed on AWS.
* **CD with GitHub Actions**: Automated deployment and integration using GitHub Actions.
* **Infrastructure as Code**: Uses Terraform for creating and managing infrastructure.

## Folder Structure

Automated tests are usually placed into the `test` or, less commonly, into the `spec` or `tests` folder.

> **Q: Why tests are placed into a separate folder, as opposed to having them closer to the code under test?**
>
> **A:** Because you don't want to test the code, you want to test the *program*.

    .
    ├── ...
    ├── test                    # Test files (alternatively `spec` or `tests`)
    │   ├── benchmarks          # Load and stress tests
    │   ├── integration         # End-to-end, integration tests (alternatively `e2e`)
    │   └── unit                # Unit tests
    └── ...

> **Samples**: [jQuery](https://github.com/jquery/jquery), [Node.js](https://github.com/joyent/node), [D3.js](https://github.com/mbostock/d3), [AngularJS](https://github.com/angular/angular.js), [Adobe Brackets](https://github.com/adobe/brackets), [three.js](https://github.com/mrdoob/three.js), [Express](https://github.com/visionmedia/express), [Socket.IO](https://github.com/LearnBoost/socket.io), [Less.js](https://github.com/less/less.js), [Bower](https://github.com/bower/bower), [Mozilla PDF.js](https://github.com/mozilla/pdf.js), [Grunt](https://github.com/gruntjs/grunt), [Gulp](https://github.com/gulpjs/gulp), [Semantic UI](https://github.com/Semantic-Org/Semantic-UI), [Zepto.js](https://github.com/madrobby/zepto), [Jade](https://github.com/visionmedia/jade), [RethinkDB](https://github.com/rethinkdb/rethinkdb), [Vagrant](https://github.com/mitchellh/vagrant), [Sails.js](https://github.com/balderdashy/sails), [GitHub Hubot](https://github.com/github/hubot), [Facebook React](https://github.com/facebook/react), [Ansible](https://github.com/ansible/ansible), [ASP.NET](https://aspnetwebstack.codeplex.com/SourceControl/latest), [browserify](https://github.com/substack/node-browserify), [Paper.js](https://github.com/paperjs/paper.js), [Julia](https://github.com/JuliaLang/julia), [Karma](https://github.com/karma-runner/karma)

