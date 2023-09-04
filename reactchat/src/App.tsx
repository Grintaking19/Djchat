import {
  createBrowserRouter,
  createRoutesFromElements,
  Route,
  RouterProvider,
} from "react-router-dom";

import Home from "./pages/Home";
import Explore from "./pages/Explore";
import React from "react";
import { ThemeProvider } from "@emotion/react";
import { createMuiTheme} from "./theme/theme.tsx"

// Create a router that uses the native browser history under the hood.
const router = createBrowserRouter((
  createRoutesFromElements(
    <Route>
      <Route path="/" element={<Home />} />
      <Route path="/explore/:categoryName" element={<Explore />} />
     </Route>
   )
  )
);

// The root component of our app is just the router provider that
const App: React.FC = () => {
  return (
    <ThemeProvider theme={createMuiTheme()}>
      <RouterProvider router={router} />
    </ThemeProvider>
  );
};

export default App;
