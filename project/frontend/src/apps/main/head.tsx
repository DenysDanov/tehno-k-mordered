import { Component } from 'react';
import { HeadProvider, Title } from 'react-head';

import '../../static/styles/fancybox.scss'
import '../../static/styles/formstyler.scss'
import '../../static/styles/normalize.scss'
import '../../static/styles/slick.scss'
import '../../static/styles/index.scss'
import '../../static/styles/dev_1_adapt.scss'

export class Head extends Component{
    render(){
        return (
            <HeadProvider>
                <Title>Website</Title>
            </HeadProvider>
        )
    }    
}