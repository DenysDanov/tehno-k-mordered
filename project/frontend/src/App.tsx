import { Fragment, useState } from 'react';
import './App.css';
import { News } from './apps/news/news';
import OnLoadingUserData from './apps/loading';

import {ScriptsPage} from './apps/main/scripts'
import { Head } from './apps/main/head';

function App() {
  const [NewsLoaded, SetNewsLoaded] = useState<{state : boolean}>({state: false});
  const NewsComponent = OnLoadingUserData(News, 'http://localhost:8000/news/', NewsLoaded.state, SetNewsLoaded)
  
  const [CategoryLoaded, setCategoryLoaded] = useState<{state : boolean}>({state: false});
  


  return (
    <Fragment>
      <Head />
      <ScriptsPage />
      <NewsComponent />
    </Fragment>
  );
}

export default App;
