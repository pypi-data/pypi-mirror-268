import { Streamlit, RenderData } from "streamlit-component-lib"
import { forwardDesktopApiMethodCallToPlatform } from "./desktop";
import { forwardOntologyApiMethodCallToPlatform } from "./ontology";

/**
 * The component's render function. This will be called immediately after
 * the component is initially loaded, and then again every time the
 * component gets new data from Python.
 */
function onRender(event: Event): void {
  // console.log(event);
  // Get the RenderData from the event
  const data = (event as CustomEvent<RenderData>).detail;

  // Maintain compatibility with older versions of Streamlit that don't send
  // a theme object.
  // if (data.theme) {
  //   // Use CSS vars to style our button border. Alternatively, the theme style
  //   // is defined in the data.theme object.
  //   console.log(data.theme);
  // }

  console.log(data.args);

  if (!data.args) {
    throw new Error("No call definition passed to the component!");
  }

  const service = data.args["service"];

  // Streamlit.setFrameHeight(0);

  switch (service) {
    case "desktop":
      Promise.resolve(forwardDesktopApiMethodCallToPlatform(data.args)).then(
        (result) => {
          Streamlit.setComponentValue(result);
          Streamlit.setFrameHeight();
        }
      );
      break;

    case "ontology":
      Promise.resolve(forwardOntologyApiMethodCallToPlatform(data.args)).then(
        (result) => {
          Streamlit.setComponentValue(result);
          Streamlit.setFrameHeight();
        }
      );
      break;

    default:
      throw new Error(`Call to an unknown service: ${service}`);
  }

  // We tell Streamlit to update our frameHeight after each render event, in
  // case it has changed. (This isn't strictly necessary for the example
  // because our height stays fixed, but this is a low-cost function, so
  // there's no harm in doing it redundantly.)
  Streamlit.setFrameHeight();
}

// Attach our `onRender` handler to Streamlit's render event.
Streamlit.events.addEventListener(Streamlit.RENDER_EVENT, onRender)

// Tell Streamlit we're ready to start receiving data. We won't get our
// first RENDER_EVENT until we call this function.
Streamlit.setComponentReady()

// Finally, tell Streamlit to update our initial height. We omit the
// `height` parameter here to have it default to our scrollHeight.
Streamlit.setFrameHeight()
