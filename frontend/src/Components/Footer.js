import React, { Component } from 'react';

class Footer extends Component {
    render(){
        return(
            <footer style={{backgroundColor: '#222', textAlign: 'center', color: 'white', width: '100%', padding: '10px 0 10px 0'}}>
                <p>
                    Designed and developed by Unicode.
                    <br/><br/>
                    <a href="https://github.com/djunicode/DJ-Comps-Book-Exchange" target="_blank" rel="noopener noreferrer">
                        <img src="logo.png" width="20px" height="20px" alt="GitHub Repository"/>
                    </a>
                </p>
            </footer>
        );
    }
}

export default Footer;
