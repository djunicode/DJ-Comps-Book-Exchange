import React from 'react';
import Drawer from 'material-ui/Drawer';
import MenuItem from 'material-ui/MenuItem';
import RaisedButton from 'material-ui/RaisedButton';
import Avataar from './Avatar.js'
import { Link } from 'react-router-dom'
import { Container, Row, Col } from 'reactstrap';

export default class NavBar extends React.Component {

  constructor(props) {
    super(props);
    this.state = {open: false};
  }

  handleToggle = () => this.setState({open: !this.state.open});

  handleClose = () => {
  	this.setState({open: false});
  }

  render() {
    return (
      <div style={{marginLeft: 20}}>
         <Col><RaisedButton label="Expand" onClick={this.handleToggle} style={{height: 40, margin: "-5px -20px 10px -20px"}}/></Col>
         <Col></Col>
      
        <Drawer containerStyle={{backgroundColor: "lightgray"}}
          docked={false}
          width={200}
          open={this.state.open}
          onRequestChange={(open) => this.setState({open})}
        >
          <div style={{padding: "10px 0px 0px 20px", backgroundColor: "white"}}>
          	<h3>Welcome</h3>
          	<Avataar name="Elon Musk"></Avataar> <hr/>
          </div>
          <MenuItem onClick={this.handleClose}><Link to='/'>Home</Link></MenuItem>
          <MenuItem onClick={this.handleClose}><Link to='/forum'>Forum</Link></MenuItem>
          <MenuItem onClick={this.handleClose}><Link to='/chatbox'>ChatBox</Link></MenuItem>
          <MenuItem onClick={this.handleClose}><Link to='/inventory'>Inventory</Link></MenuItem>
          <MenuItem onClick={this.handleClose}><Link to='/profile'>Profile</Link></MenuItem>
          <MenuItem onClick={this.handleClose}><Link to='/logout'>Sign Out</Link></MenuItem>
        </Drawer>
      </div>
    );
  }
}


const styles={
	heading:{
		fontFamily: 'Tangerine',
        fontSize: 50,
        marginLeft: "32%",
        float: "left"
	}
}