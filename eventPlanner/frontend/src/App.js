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

import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Navigation from "./components/Navigation";
import Profile from "./components/Profile";
import Contact from "./components/Contact";
import SelectDateTime from "./components/SelectDateTimeAndCategory";
import { Layout } from "antd";
import Navbar from "./components/Navbar/Navbar";
import SelectDateTimeAndCategory from "./components/SelectDateTimeAndCategory";
import Events from './components/Events';
const { Header, Content, Footer, Sider } = Layout;


function App() {

  return (
    <div className="App">
      <Router>
        <Navbar/>
        <Switch>
          <Route path="/" exact component={() => 
          <Content style={{ padding: '0 24px', minHeight: 280 }}>
            <SelectDateTimeAndCategory />
            </Content>} />
          <Route path="/profile" exact component={() => <Profile />} />
          <Route path="/contact" exact component={() => <Contact />} />
          <Route path="/events" exact component={() => 
          <Content style={{ padding: '0 24px 10px 24px ', minHeight: 280, marginBottom: 100}}>
             <Events />
          </Content>} />   
        </Switch>
      </Router>
      <Footer className = "mt4" style={{ textAlign: 'center' }}>OOSE GROUP 8</Footer>
    </div>
  );
}

export default App;
