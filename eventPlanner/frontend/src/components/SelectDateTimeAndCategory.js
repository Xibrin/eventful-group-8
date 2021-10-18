import React, {useState} from "react";
import { Calendar, TimePicker, Card, Tag, Button} from 'antd';
import "./styles/stylesheet.css";
import basscss from 'basscss/css/basscss.min.css';
const {CheckableTag} = Tag;

const sports = "soccer basketball tennis baseball golf running volleyball badminton swimming boxing table  ice-skating roller cricket rugby pool darts football bowling ice hockey surfing karatehorse racing snowboarding skateboarding cycling archery fishing gymnastics figure rock climbing sumo wrestling taekwondo fencing water jet weight lifting"
const sportsList = sports.split(" ");

function onPanelChange(value, mode) {
    console.log(value, mode);
  }

const format = 'HH:mm';

const SelectDateTimeAndCategory = () => {
    const [timeRange, setTimeRange] = useState();
    const [date, setDate] = useState();
    const [selectedTags, setSelectedTags] = useState([]);

    function onSelectDate(value) {
        setDate(value);
        console.log(value);
    }
    
    function onSelectTime(value) {
        setTimeRange(value);
        //console.log(value);
    }
    function handleChange(tag, checked) {
        const nextSelectedTags = checked ? [...selectedTags, tag] : selectedTags.filter(t => t !== tag);
        console.log('You are interested in: ', nextSelectedTags);
        setSelectedTags(nextSelectedTags);
    }
    
    const isComplete = timeRange && date;
    return (
        <>
        <Card title="When are you free?" bordered={false} >
        <div className = "clearfix">
            <div className="site-calendar-demo-card col col-6">
                <Calendar fullscreen={false} onPanelChange={onPanelChange} onSelect={onSelectDate}/>
            </div>
            <div className = "col col-6 flex">
            <h5 className = "ml2 mr2">Start Time / End Time: </h5>
            <TimePicker.RangePicker format={format} onChange = {onSelectTime}/>
            {timeRange && console.log(timeRange)}
            </div>
        </div>
        </Card>
        <div className = "mt2">
            {isComplete && 
            <>
            <h5 className = "center">Categories</h5>
            <div className = "mx-auto" style = {{width: 550,  alignItems: "center"}}>
                <Card size = "large">
                {sportsList.map((item) => (
                        <CheckableTag key = {item} checked={
                            selectedTags.indexOf(item) > -1 }
                        onChange={checked => handleChange(item, checked)}>{item}</CheckableTag>
                 ))
                }
                </Card>
                <Button className = "mt1 right" type= "primary">Submit</Button>
            </div>
            </>}
        </div>
        </>
    )
}

export default SelectDateTimeAndCategory;
  

