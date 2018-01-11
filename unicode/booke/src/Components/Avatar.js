import React from 'react';
import Avatar from 'material-ui/Avatar';
import FileFolder from 'material-ui/svg-icons/file/folder';
import FontIcon from 'material-ui/FontIcon';
import List from 'material-ui/List/List';
import ListItem from 'material-ui/List/ListItem';

import {
  blue300,
  indigo900,
  orange200,
  deepOrange300,
  pink400,
  purple500,
} from 'material-ui/styles/colors';

const style = {margin: 5};

/**
 * Examples of `Avatar` using an image, [Font Icon](/#/components/font-icon), [SVG Icon](/#/components/svg-icon)
 * and "Letter" (string), with and without custom colors at the default size (`40dp`) and an alternate size (`30dp`).
 */
const Avataar = () => (
  <List>
    <ListItem
      disabled={true}
      leftAvatar={
        <Avatar src="https://pbs.twimg.com/profile_images/782474226020200448/zDo-gAo0_400x400.jpg" />
      }
    >
      Elon Musk
    </ListItem>
  </List>
);

export default Avataar;