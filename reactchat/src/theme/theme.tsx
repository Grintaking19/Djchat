import { createTheme, responsiveFontSizes } from '@mui/material'

// This is the theme interface, it is used to define the theme object
// This is like extending the Theme interface from @mui/material
declare module '@mui/material/styles' {
  interface Theme {
    primaryAppBar: {
      height: number;
    };
    primaryDrawer: {
      width: number;
      onCloseWidth: number;
    };
  }
  // allow configuration using `createTheme`
  interface ThemeOptions {
    primaryAppBar?: {
      height?: number;
    };
    primaryDrawer: {
      width: number;
      onCloseWidth: number;
    };
  }
}

// This is the theme creator, 
// it is used to create a theme object that can be used in the app
export const createMuiTheme = () => {
  let theme = createTheme({
    
    typography: {
      fontFamily: ['IBM Plex Sans', 'sans-serif'].join(','),
    },
    
    primaryAppBar: {
      height: 50,
    },
    primaryDrawer: {
      width: 240,
      onCloseWidth: 70,
    },
    components: {
      MuiAppBar: {
        defaultProps: {
          elevation: 0,
          color: 'default'
        }
      }
    }
  })
  theme = responsiveFontSizes(theme);
  return theme;
};

export default createMuiTheme;