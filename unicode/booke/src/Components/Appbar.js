import React, {Component} from 'react';
import AppBar from 'material-ui/AppBar';
import IconButton from 'material-ui/IconButton';
import IconMenu from 'material-ui/IconMenu';
import MenuItem from 'material-ui/MenuItem';
import FlatButton from 'material-ui/FlatButton';
import Toggle from 'material-ui/Toggle';
import MoreVertIcon from 'material-ui/svg-icons/navigation/more-vert';
import NavigationClose from 'material-ui/svg-icons/navigation/close';
import NavBar from './NavBar';
import Drawer from 'material-ui/Drawer';
import Divider from 'material-ui/Divider';
import Avataar from './Avatar';
import { Link } from 'react-router-dom';

class Login extends Component {
  static muiName = 'FlatButton';

  render() {
    return (
      <FlatButton {...this.props} label="Login" />
    );
  }
}

const Logged = (props) => (
  <IconMenu
    {...props}
    iconButtonElement={
      <IconButton><MoreVertIcon /></IconButton>
    }
    targetOrigin={{horizontal: 'right', vertical: 'top'}}
    anchorOrigin={{horizontal: 'right', vertical: 'top'}}
  >
    <MenuItem primaryText="Refresh" />
    <MenuItem primaryText="Help" />
    <MenuItem primaryText="Sign out" />
  </IconMenu>
);

Logged.muiName = 'IconMenu';

class AppBarExampleComposition extends Component {
  state = {
    logged: false,
  };

  handleChange = (event, logged) => {
    this.setState({logged: logged});
  };
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
      <div>
        
        <AppBar
          title="Book-e"          
          
          iconElementRight={this.state.logged ? <Logged /> : <Login />}
          onLeftIconButtonClick={this.handleToggle}
          titleStyle={{textAlign:'center'}}
        />

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

export default AppBarExampleComposition;

