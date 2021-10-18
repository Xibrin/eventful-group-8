// import React from "react";
// import 'antd/dist/antd.css';
// import {  Layout, Menu, Breadcrumb  } from "antd";
// import {  UserOutlined, LaptopOutlined, NotificationOutlined  } from "@ant-design/icons";
// import SelectDateTime from "./components/SelectDateTime";
// import Navigation from "./components/Navigation";
// import Profile from "./components/Profile";
// import Contact from "./components/Contact";
// import { Route, Switch, Router } from "react-router-dom";
// const { SubMenu } = Menu;
// const { Header, Content, Footer, Sider } = Layout;


// function App() {
//   return (
//       <div className = "App" >
//         <Router>
//         <Navigation />
//         <Switch>
//           <Route path="/" exact component={() => <SelectDateTime />} />
//           <Route path="/about" exact component={() => <Profile />} />
//           <Route path="/contact" exact component={() => <Contact />} />
//         </Switch>
//       </Router>
//       </div>
//     );
// }

// export default App;

import React from "react";
import Card from "./components/Card";
import food from "./components/assets/Logo.jpeg"
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Navigation from "./components/Navigation";
import Profile from "./components/Profile";
import Contact from "./components/Contact";
import SelectDateTime from "./components/SelectDateTimeAndCategory";
import { Layout } from "antd";
import Navbar from "./components/Navbar/Navbar";
import SelectDateTimeAndCategory from "./components/SelectDateTimeAndCategory";
const { Header, Content, Footer, Sider } = Layout;


function App() {
  const EventOrganizer = "NFL";
  const Event = {
    title: "Super Bowl LII",
    date: "February 14, 2021",
    image: food,
    description:
      "Super Bowl LI featuring the ___ vs ___. Blah blah blah blah blah Blah blah blah blah blah Blah blah blah blah blah Blah blah blah blah blah Blah blah blah blah blah Blah blah blah blah blah",
  };

  return (
    <div className="App">
      <Router>
        <Navbar/>
        <Switch>
          <Route path="/" exact component={() => 
          <Content style={{ padding: '0 24px', minHeight: 280 }}>
            <SelectDateTimeAndCategory />
            <Card
          author={EventOrganizer}
          title={Event.title}
          date={Event.date}
          description={Event.description}
        />
            </Content>} />
          <Route path="/about" exact component={() => <Profile />} />
          <Route path="/contact" exact component={() => <Contact />} />
        </Switch>
      </Router>
      <Footer className = "mt4" style={{ textAlign: 'center' }}>OOSE GROUP 8</Footer>
    </div>
  );
}

export default App;
