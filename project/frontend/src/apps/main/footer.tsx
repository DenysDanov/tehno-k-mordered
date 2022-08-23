import { Component, Fragment } from "react";
import { ICategory } from "../models/category";

interface IFooter{
    result: ICategory[]
}

export class Footer extends Component<IFooter>{

    render(){
        return(
            <Fragment>
                <footer className="footer">
                
                </footer>

            </Fragment>
        )
    }
}