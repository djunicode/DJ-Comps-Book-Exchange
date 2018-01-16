import React, {Component} from 'react';
import {Container} from 'reactstrap';

class Logout extends Component {
  render() {
    return (
      <div>
          <Container>
            <h1 style={{textAlign: 'center'}}>Logged Out</h1>
          </Container>
      </div>
    );
  }
}

export default Logout;
