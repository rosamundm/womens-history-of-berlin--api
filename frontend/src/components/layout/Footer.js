import React, { Component } from "react";

class Footer extends Component {
    render () {
        return (
           <div className="contact-copyright">
             <p>© Rosamund Mather {(new Date().getFullYear())}</p>
           </div>
        )
    }
};

export default Footer;
