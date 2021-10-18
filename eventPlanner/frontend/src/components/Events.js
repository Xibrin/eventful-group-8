import React from 'react';
import Card from './Card'
import food from "./assets/Logo.jpeg"
import basscss from 'basscss/css/basscss.min.css';

const EventOrganizer = "NFL";
  const Event = {
    title: "Super Bowl LII",
    date: "February 14, 2021",
    image: food,
    description:
      "Super Bowl LI featuring the ___ vs ___. Blah blah blah blah blah Blah blah blah blah blah Blah blah blah blah blah Blah blah blah blah blah Blah blah blah blah blah Blah blah blah blah blah",
  };

const Events = () => {
    return (
        <div className = "mt2 mb4 pb4"> 
        <h1 className = "center">Events</h1>
        <Card
          author={EventOrganizer}
          title={Event.title}
          date={Event.date}
          description={Event.description}
        /> 
        <Card
          author={EventOrganizer}
          title={Event.title}
          date={Event.date}
          description={Event.description}
        /> 
        <Card
          author={EventOrganizer}
          title={Event.title}
          date={Event.date}
          description={Event.description}
        /> 
        </div>
    )
}

export default Events;