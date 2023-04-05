function sendValue(value) {
    Streamlit.setComponentValue(value)
}

/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */
function onRender(event) {
    if (!window.rendered) {
        let igvDiv = document.getElementById("igv");
        let params = event.detail.args['params']
        igv.createBrowser(igvDiv, params)
            .then(function (browser) {
                console.log("Created IGV browser");
            })
    }
}

Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)
Streamlit.setComponentReady()
Streamlit.setFrameHeight(600)
