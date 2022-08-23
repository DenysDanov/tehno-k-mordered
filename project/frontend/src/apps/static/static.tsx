import { Component, Fragment } from "react";
import {Link} from 'react-head'
interface IStatic{
    url: string    
};

const STATIC_URL = 'http://localhost:8000/static/';

export class StaticImg extends Component<IStatic>{
    render(){
        return (
            <Fragment>
                <img src={STATIC_URL + this.props.url} />
            </Fragment>
        )
    }
}

export class StaticStyle extends Component<IStatic>{
    render(){
        return (
            <Fragment>
                <Link rel="stylesheet" href={STATIC_URL + this.props.url} />
            </Fragment>
        )
    }
}

export class StaticScript extends Component<IStatic>{
    render(){
        return (
            <Fragment>
                <script src={STATIC_URL + this.props.url} />
            </Fragment>
        )
    }
}
