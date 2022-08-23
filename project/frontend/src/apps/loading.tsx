import axios from "axios"
import React, { useState } from "react"

function OnLoadingUserData(Component: any, api_url: string, isLoaded:any, setter: React.Dispatch<React.SetStateAction<{state: boolean}>>) {
    const [p, setProps] = useState<{result: any}>()
    
    if (isLoaded === false) {
        axios.get(api_url).then(
            (resp: any) => {
                setProps({result: resp.data})
                setter({state: true});
                
                console.log(resp.data)
            }
        )
    }
    return function LoadingPersonsData() {
        if (isLoaded === true) return <Component {...p} />

        else return (
            <div>
                <h1>Подождите, данные загружаются!</h1>
            </div>
        )
    }
}

export default OnLoadingUserData