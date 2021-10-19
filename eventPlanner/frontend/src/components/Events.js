import React from 'react';
import Card from './Card'
import food from "./assets/Logo.jpeg"
import axios from 'axios';
import { Component } from 'react';
import basscss from 'basscss/css/basscss.min.css';

  class Events extends Component {
    constructor(props) {
      super(props);
      this.state = {
        eventList: []
      }
    }

    componentDidMount() {
      axios.get('localhost:8000/events')
      //Add start date/time and end date/time
      .then(
        response => {
          console.log(response)
          this.setState({eventList: response.data})
        } 
      )
      .catch(error => {console.log(error)})
    }
    

    render() {
      const { eventList } = this.state;
      return (
        <div className = "mt2 mb8 pb4"> 
        <h1 className = "center">Events</h1>
        {
          eventList.length ?
          eventList.map(event => 
          <Card
            author={event.name[0]}
            title={event.name}
            date={event.start_time}
            description={event.info}
          /> ):
          null
        }
        </div>
    );
    }
  }
  
  export default Events;
