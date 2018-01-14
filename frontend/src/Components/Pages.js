import React from 'react'
import { Switch, Route } from 'react-router-dom'
import Home from './Pages/Home.js'
import Forum from './Pages/Forum.js'
import ChatBox from './Pages/ChatBox.js'
import Inventory from './Pages/Inventory.js'
import Profile from './Pages/Profile.js'
import Logout from './Pages/Logout.js'

const Pages = () => (
  <main>
    <Switch>
      <Route exact path='/' component={Home}/>
      <Route path='/forum' component={Forum}/>
      <Route path='/chatbox' component={ChatBox}/>
      <Route path='/inventory' component={Inventory}/>
      <Route path='/profile' component={Profile}/>
      <Route path='/logout' component={Logout}/>
    </Switch>
  </main>
)

export default Pages;
