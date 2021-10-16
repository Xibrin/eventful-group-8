import React, {useState} from "react";
import { Calendar, TimePicker, Card} from 'antd';
import "./styles/calendarStyle.css";
import basscss from 'basscss/css/basscss.min.css';

function onPanelChange(value, mode) {
    console.log(value, mode);
  }

// function onChange(event) {
//     console.log(event.target.value);
// }

const format = 'HH:mm';

const SelectDateAndTime = () => {
    const [timeRange, setTimeRange] = useState();
    const [date, setDate] = useState();

    function onSelectDate(value) {
        setDate(value);
        console.log(value);
    }
    
    function onSelectTime(value) {
        setTimeRange(value);
        //console.log(value);
    }

    return (
        <Card title="When are you free?" bordered={false} >
        <div className = "clearfix">
            <div className="site-calendar-demo-card col col-6">
                <Calendar fullscreen={false} onPanelChange={onPanelChange} onSelect={onSelectDate}/>
            </div>
            <div className = "col col-6 flex">
            <h3 className = "ml2 mr2">Start Time / End Time: </h3>
            <TimePicker.RangePicker format={format} onChange = {onSelectTime}/>
            {timeRange && console.log(timeRange)}
            </div>
        </div>
        </Card>
    )
}

export default SelectDateAndTime;
  

