import React, {Component} from 'react';
import AppBar from 'material-ui/AppBar';
import IconButton from 'material-ui/IconButton';
import IconMenu from 'material-ui/IconMenu';
import Menu from 'material-ui/Menu';
import MenuItem from 'material-ui/MenuItem';
import FlatButton from 'material-ui/FlatButton';
import Toggle from 'material-ui/Toggle';
import MoreVertIcon from 'material-ui/svg-icons/navigation/more-vert';
import Drawer from 'material-ui/Drawer';
import Divider from 'material-ui/Divider';
import UserAvatar from './UserAvatar';
import {Link} from 'react-router-dom';

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
    <MenuItem primaryText="My Profile" />
    {/*<MenuItem primaryText="Help" />*/}
    <MenuItem primaryText="Sign out" />
  </IconMenu>
);

const style = {
  display: 'inline-block',
  margin: '16px 32px 16px 0',
  float: 'left',
  width: '250px',
  textAlign: 'center',
};

Logged.muiName = 'IconMenu';

class AppBarWithMenu extends Component {
  state = {
    logged: false,
    open: false
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
          title="Booke"
          iconElementRight={this.state.logged ? <Logged /> : <Login />}
          onLeftIconButtonClick={this.handleToggle}
          titleStyle={{textAlign:'center'}}
        />

        <Drawer
          docked={false}
          width={280}
          open={this.state.open}
          onRequestChange={(open) => this.setState({open})}
        >
            <Menu style={style}>
                <MenuItem style={{textAlign: 'left'}} disabled={true}><h3 style={{color: 'black'}}>Welcome</h3><UserAvatar name="Elon Musk"></UserAvatar></MenuItem>
                <Divider/>
                <Link to='/' style={{textDecoration: 'none'}}><MenuItem onClick={this.handleClose}>Home</MenuItem></Link>
                <Divider/>
                <Link to='/forum' style={{textDecoration: 'none'}}><MenuItem onClick={this.handleClose}>Forum</MenuItem></Link>
                <Divider/>
                <Link to='/chatbox' style={{textDecoration: 'none'}}><MenuItem onClick={this.handleClose}>Messages</MenuItem></Link>
                <Divider/>
                <Link to='/inventory' style={{textDecoration: 'none'}}><MenuItem onClick={this.handleClose}>Inventory</MenuItem></Link>
                <Divider/>
                <Link to='/profile' style={{textDecoration: 'none'}}><MenuItem onClick={this.handleClose}>Profile</MenuItem></Link>
                <Divider/>
                <Link to='/logout' style={{textDecoration: 'none'}}><MenuItem onClick={this.handleClose}>Sign Out</MenuItem></Link>
                <Divider/>
            </Menu>
        </Drawer>
        <Toggle
          label="Logged"
          defaultToggled={false}
          onToggle={this.handleChange}
          labelPosition="right"
          style={{margin: 20}}
        />
      </div>
    );
  }
}

export default AppBarWithMenu;
