# Team14App

URL fishing detection application containing frontend and service
This project was generated with [Angular CLI](https://github.com/angular/angular-cli) version 17.3.7.

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The application will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory.

## Further help

To get more help on the Angular CLI use `ng help` or go check out the [Angular CLI Overview and Command Reference](https://angular.io/cli) page.


## App service

It has a version service to ask for the library version from the lib-version service.
It has a url service to send a post request to the model service.

## Usage

To configure the URL of the model service e.i. the api endpoint that handles the prediction, edit the `environment.ts` file and set `modelServiceURL="your_url"`
Navigate to team14-app folder and run `ng serve` to start the application.

On the webpage you can provide a link and select a model to then predict if the given link is spam or ham.
The library version is displayed on the webpage.
