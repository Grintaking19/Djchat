import React from 'react';
import  PrimaryAppBar  from './templates/PrimaryAppBar.tsx';
import PrimaryDrawer from './templates/PrimaryDraw.tsx';
import { Box, CssBaseline } from '@mui/material';
import SecondaryDrawer from './templates/SecondaryDrawer.tsx';


const Home: React.FC = () => {
  return (
    <Box sx={{ display: "flex" }}>
      <CssBaseline />
      <PrimaryAppBar />
      <PrimaryDrawer />
      <SecondaryDrawer />
      <p>home</p>
      <p>Coming soon...</p>
    </Box>
  );
}

export default Home;
