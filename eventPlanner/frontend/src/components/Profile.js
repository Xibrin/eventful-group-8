import React from "react";
import "./styles/Profile.css"
import Card from "./Card";
import food from "./assets/Logo.jpeg"
import basscss from 'basscss/css/basscss.min.css';


function Profile() {
return (
    
<div className="mx-auto">
    <div className="title">
        Profile
    </div>
    <div className="special">
        <form id="my-form">
            <div className="heading"> UserFirstName UserLastName </div>
            <div className="picture mx-auto"> <img src={food} alt={food}/></div>
            <div className="profileSection">
                About you:
            </div>
            <div className="profileSection">
                Categories:
                <div className="categories">
                    Blah Blah
                </div>
                <div className="categories">
                    Blah Blah
                </div>
                <div className="categories">
                    Blah Blah
                </div>
            </div>
            <div className="profileSection">
                Saved Location:
            </div>
            <div className="profileSection">
                Schedule
            </div>
        </form>
    </div>

</div>
);

}

export default Profile;