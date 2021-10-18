import React from "react";
import 'antd/dist/antd.css';
import { ReactDOM } from "react";
import { Link, withRouter } from "react-router-dom";
import {  Layout, Menu, Typography, Avatar } from "antd";
import "@fortawesome/fontawesome-free/css/all.css";


const { SubMenu } = Menu;
const { Header } = Layout;
const {Title} = Typography;


function Navigation(props) {

  return (
    <Layout className="layout">
    <Header style = {{padding:10}}>

    <i class="fas fa-skating"></i>
      <Title>EventFull</Title>
  
    </Header>
  </Layout>
  )
}

export default withRouter(Navigation);

// import React from "react";
// import { Link, withRouter } from "react-router-dom";

// function Navigation(props) {
//   return (
//     <div className="navigation">
//       <nav class="navbar navbar-expand navbar-dark bg-dark">
//         <div class="container">
//           <Link class="navbar-brand" to="/">
//             React Multi-Page Website
//           </Link>
//           <div>
//             <ul class="navbar-nav ml-auto">
//               <li
//                 class={`nav-item  ${
//                   props.location.pathname === "/" ? "active" : ""
//                 }`}
//               >
//                 <Link class="nav-link" to="/">
//                   Home
//                   <span class="sr-only">(current)</span>
//                 </Link>
//               </li>
//               <li
//                 class={`nav-item  ${
//                   props.location.pathname === "/about" ? "active" : ""
//                 }`}
//               >
//                 <Link class="nav-link" to="/about">
//                   About
//                 </Link>
//               </li>
//               <li
//                 class={`nav-item  ${
//                   props.location.pathname === "/contact" ? "active" : ""
//                 }`}
//               >
//                 <Link class="nav-link" to="/contact">
//                   Contact
//                 </Link>
//               </li>
//             </ul>
//           </div>
//         </div>
//       </nav>
//     </div>
//   );
// }

// export default withRouter(Navigation);
