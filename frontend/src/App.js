import React, { Component } from 'react';
//import './App.css';
//import { Container } from 'reactstrap';
import AppBarWithMenu from './Components/AppBarWithMenu'
import Pages from './Components/Pages';
import Footer from './Components/Footer';

class App extends Component {
  render() {
    return (
      <div>
        <AppBarWithMenu/>
        <Pages/>
        <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
        <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
        <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
        <Footer/>
      </div>
    );
  }
}

export default App;
