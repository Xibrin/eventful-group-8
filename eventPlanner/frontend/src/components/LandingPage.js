import React from "react";
import {Button} from 'antd';
import { Link } from "react-router-dom";
import "./styles/LandingPage.css"

function LandingPage() {
return (
<div className="mx-auto">
    <Button className="get-started" type="primary" style = {{width: 550,  alignItems: "center"}}><Link to="/home">Get Started!</Link></Button>
</div>
);

}

export default LandingPage;