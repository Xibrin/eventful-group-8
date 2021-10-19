import React from "react";
import {Nav, NavLink, Bars, NavMenu, NavBtn, NavBtnLink} from "./NavBarElements";
import "@fortawesome/fontawesome-free/css/all.css";
import "basscss/css/basscss.min.css"

const Navbar = () => {
    return (
        <Nav>
            <NavLink to = "/">
                <div className = "mr2"> <i className="fas fa-skating fa-3x"></i>
                </div>
                <div className = "mt2">
                <h1 style ={{color:'white'}}>EventFul</h1>
                </div>
            </NavLink>   
            <Bars/>
            <NavMenu>
                <NavLink to = "/home" activeStyle>
                    Home
                </NavLink>
                <NavLink to = "/profile" activeStyle>
                    Profile
                </NavLink>
                <NavLink to = "/contact" activeStyle>
                    Contact Us
                </NavLink>
            </NavMenu>
            <NavBtn>
                <NavBtnLink to = "/signin">Sign In</NavBtnLink>
            </NavBtn>     
    </Nav>
    )
}

export default Navbar;