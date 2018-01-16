import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import MuiThemeProvider from 'material-ui/styles/MuiThemeProvider';
//import 'bootstrap/dist/css/bootstrap.css';
import {BrowserRouter} from 'react-router-dom'

const page = (
	<MuiThemeProvider>
		<BrowserRouter>
			<App/>
		</BrowserRouter>
	</MuiThemeProvider>
);

ReactDOM.render(page, document.getElementById('root'));
registerServiceWorker();
