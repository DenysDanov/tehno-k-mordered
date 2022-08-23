import {Component} from "react";

import URLS from "../../prefs"

import { IUser } from "../models/auth/interface";

export interface INews{
    id : number,
    author?: IUser,
    is_published: boolean,
    publish_date: string,

    title: string,
    descr: string,
    image: string,

    introduction?: string,
    conclusion?: string,

    slug: string,
    
    subtitles?: Array<ISubtitle>,
}

export interface ISubtitle{
    article: INews
    subtitle: string,
    text: string
}


interface NewsProps{
    result : INews[]
}

export class News extends Component<NewsProps> {
    render (){
        
        return(
            
        <div className="news-section section sub-section">
            
            <div className="wrapper">
                <div className="section-title sub-section-title title">
                    <h2>Новости компании</h2>
                </div>
                <div className="news-blocks">
                    
                    {this.props.result.map(
                        obj => 
                        <div className="item" key={obj.id}>
                        <a href={URLS.API_URL + `news/${obj.slug}`} className="item-image">
                            <img src={obj.image} alt="News" />
                        </a>
                        <div className="item-content">
                            <div className="post-date">
                                <span>{ obj.publish_date }</span>
                            </div>
                            <a href={URLS.API_URL + `news/${obj.slug}`} className="item-title title">
                                <h4>{ obj.title }</h4>
                            </a>
                            <div className="item-text text">
                                <p>{ obj.descr }</p>
                            </div>
                            <div className="read-all">
                                <a href={URLS.API_URL + `news/${obj.slug}`}>Читать подробнее</a>
                            </div>
                        </div>
                    </div>
                    )}
                </div>
            </div>
        </div>)
    }
}