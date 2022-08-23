import { Component, Fragment } from "react";
import { StaticScript } from "../static/static";

export class ScriptsPage extends Component{
    render(){
        return(
            <Fragment>
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>
                <StaticScript url="scripts/plagins/device.js"/>
                <StaticScript url="scripts/validate_script.js"/>
                <StaticScript url="scripts/validate_script.js"/>
                <StaticScript url="scripts/plagins.js"/>
                <StaticScript url="scripts/plagins/device.js"/>
                <StaticScript url="scripts/plagins/jquery.fancybox.min.js"/>
                <StaticScript url="scripts/plagins/jquery.formstyler.min.js"/>
                <StaticScript url="scripts/plagins/jquery.validate.min.js"/>
                <StaticScript url="scripts/plagins/maskInput.js"/>
                <StaticScript url="scripts/plagins/slick.js"/>
                <StaticScript url="scripts/main.js"/>
                <StaticScript url="scripts/develop/develop_1.js"/>
            </Fragment>
        )
    }
}

// <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js"></script>

// <!-- build:js  -->
// <script type="text/javascript" src="{% static '' %}" ></script>
// <!-- endbuild -->

// <!-- build:js  -->
// <script type="text/javascript" src="{% static '' %}" ></script>
// <script type="text/javascript" src="{% static '' %}" ></script>
// <script type="text/javascript" src="{% static '' %}" ></script>
// <script type="text/javascript" src="{% static '' %}" ></script>
// <script type="text/javascript" src="{% static '' %}" ></script>
// <script type="text/javascript" src="{% static '' %}" ></script>
//     <!-- add you plagins js here -->

// <!-- endbuild -->

// <!-- build:js  -->
// <script type="text/javascript" src="{% static '' %}" ></script>
// <script type="text/javascript" src="{% static 'scripts/develop/develop_1.js' %}" ></script>
//     <!-- add you develop js here -->
// <!-- endbuild -->

// <!-- /SCRIPTS -->