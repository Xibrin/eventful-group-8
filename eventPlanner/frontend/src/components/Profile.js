import React from "react";
import "./styles/Profile.css"
import food from "./assets/Logo.jpeg"
import { Card, Avatar } from "antd";
import basscss from 'basscss/css/basscss.min.css';
import Events from "./Events";
const { Meta } = Card;



const Profile = () => {
    return (
        <div className = "mx-auto">
          <h3 className = "center mt2">Profile</h3>
        <Card style={{ width: 500, marginTop: 30, marginLeft: "auto", marginRight: "auto"}}>
          <Meta
            avatar={<Avatar src="https://joeschmoe.io/api/v1/random&quot; />}
            title="FirstName LastName"
            description="About Me:"
          />
          <div className = "mt2 pt1">
            <p>Email: yourname@email.com</p>
          </div>
        </Card>
        <h5 className = "mt4">Frequently Visited Categories:</h5>
        <h5 className = "mt4">Recently Viewed Events:</h5>
        <Events/>
        </div>
   
    )
}

export default Profile;
