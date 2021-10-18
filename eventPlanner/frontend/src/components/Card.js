import React from "react";
import "./styles/Card.css";
import SelectDateTimeAndCategory from "./SelectDateTimeAndCategory";
import food from "./assets/Logo.jpeg"

export default function Card(props) {

    const showcard = SelectDateTimeAndCategory.timeRange && SelectDateTimeAndCategory.date && SelectDateTimeAndCategory.selectedTags;

  return (
      <>
      {showcard && <>
    <div className="card col col-4" padding="5px">
      <div className="card-header">
        <div className="profile">
          <span className="letter">{props.author[0]}</span>
        </div>
        <div className="card-title-group">
          <h5 className="card-title">{props.title}</h5>
          <div className="card-date">
            {props.date}</div>
        </div>
      </div>
      <img className="card-image" src={food} alt="Logo" />
      <div className="card-text">{props.description}</div>
    </div>
    </>}
    </>
  );
}