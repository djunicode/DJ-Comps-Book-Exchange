import React, { Component } from 'react';

class Footer extends Component {
    render(){
        return(
            <footer style={{backgroundColor: 'lightgrey', textAlign: 'center', color: 'black', width: '100%', padding: '10px 0 10px 0'}}>
                <p style={{fontSize:'20px', fontWeight:'700'}}>
                    Designed and developed by <a style={{textDecoration:'none', cursor:'pointer'}} href="https://github.com/djunicode/DJ-Comps-Book-Exchange" target="_blank"><span style={{color:'rgb(0, 188, 212)'}}>Unicode</span></a>
                    <br/><br/><br/>
                    <a href="https://github.com/djunicode/DJ-Comps-Book-Exchange" target="_blank">
                        <img src="logo.png" alt="Unicode" width="200px" height="80px"/>
                    </a>
                </p>
            </footer>
        );
    }
}

export default Footer;