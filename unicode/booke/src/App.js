import React, { Component } from 'react';
import './App.css';
import { Container } from 'reactstrap';
import Appbar from './Components/Appbar'
import Pages from './Components/Pages';
import Footer from './Components/Footer';

class App extends Component {
  render() {
    return (
      <div>
        <Appbar overlayStyle={{backgroundColor: "blue"}} ></Appbar>
        <Pages></Pages>
  <br/><br/><br/><br/><br/><br/><br/><br/><br/><br/><br/>
        <br/><br/><br/><br/><br/><br/><br/>
        <Footer/>
      
      </div>
    );
  }
}

export default App;
