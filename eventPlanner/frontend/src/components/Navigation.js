// import React from "react";
// import 'antd/dist/antd.css';
// import { ReactDOM } from "react";
// import { Link, withRouter } from "react-router-dom";
// import {  Layout, Menu, Breadcrumb  } from "antd";
// import {  UserOutlined, LaptopOutlined, NotificationOutlined  } from "@ant-design/icons";
// const { SubMenu } = Menu;
// const { Header, Content, Footer, Sider } = Layout;

// function Navigation(props) {
//   return (
//     <div className="navigation">
//         <Layout>
//         <div class="container">
//           <Link class="navbar-brand" to="/">
//             Event-Full
//           </Link>
//           <div>
//               <Header className="header">
//             <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>

//             <Menu.Item class={`nav-item  ${
//                   props.location.pathname === "/" ? "active" : ""
//                 }`} key="1">
//                 <Link class="nav-link" to="/">
//                   Home
//                   <span class="sr-only">(current)</span>
//                 </Link>
//             </Menu.Item>

//             <Menu.Item class={`nav-item  ${
//                   props.location.pathname === "/profile" ? "active" : ""
//                 }`} key="1">
//                 <Link class="nav-link" to="/about">
//                   Profile
//                   <span class="sr-only">(current)</span>
//                 </Link>
//             </Menu.Item>

//             <Menu.Item class={`nav-item  ${
//                   props.location.pathname === "/contact" ? "active" : ""
//                 }`} key="1">
//                     <Link class="nav-link" to="/contact">
//                   Contact Us
//                   <span class="sr-only">(current)</span>
//                 </Link>
//                 </Menu.Item>
//           </Menu>
//           </Header>
//           </div>
//         </div>
//       <Content style={{ padding: '0 50px' }}>
//           <Layout className="site-layout-background" style={{ padding: '24px 0' }}>
//             <Sider className="site-layout-background" width={200}>
//               {/* <Menu
//                 mode="inline"
//                 defaultSelectedKeys={['1']}
//                 defaultOpenKeys={['sub1']}
//                 style={{ height: '100%' }}
//               >
//                 <SubMenu key="sub1" icon={<UserOutlined />} title="subnav 1">
//                   <Menu.Item key="1">option1</Menu.Item>
//                   <Menu.Item key="2">option2</Menu.Item>
//                   <Menu.Item key="3">option3</Menu.Item>
//                   <Menu.Item key="4">option4</Menu.Item>
//                 </SubMenu>
//                 <SubMenu key="sub2" icon={<LaptopOutlined />} title="subnav 2">
//                   <Menu.Item key="5">option5</Menu.Item>
//                   <Menu.Item key="6">option6</Menu.Item>
//                   <Menu.Item key="7">option7</Menu.Item>
//                   <Menu.Item key="8">option8</Menu.Item>
//                 </SubMenu>
//                 <SubMenu key="sub3" icon={<NotificationOutlined />} title="subnav 3">
//                   <Menu.Item key="9">option9</Menu.Item>
//                   <Menu.Item key="10">option10</Menu.Item>
//                   <Menu.Item key="11">option11</Menu.Item>
//                   <Menu.Item key="12">option12</Menu.Item>
//                 </SubMenu>
//               </Menu> */}
//             </Sider>
//           </Layout>
//         </Content>
//         </Layout>
//     </div>
//   );
// }

// export default withRouter(Navigation);
import React from "react";
import { Link, withRouter } from "react-router-dom";

function Navigation(props) {
  return (
    <div className="navigation">
      <nav class="navbar navbar-expand navbar-dark bg-dark">
        <div class="container">
          <Link class="navbar-brand" to="/">
            React Multi-Page Website
          </Link>
          <div>
            <ul class="navbar-nav ml-auto">
              <li
                class={`nav-item  ${
                  props.location.pathname === "/" ? "active" : ""
                }`}
              >
                <Link class="nav-link" to="/">
                  Home
                  <span class="sr-only">(current)</span>
                </Link>
              </li>
              <li
                class={`nav-item  ${
                  props.location.pathname === "/about" ? "active" : ""
                }`}
              >
                <Link class="nav-link" to="/about">
                  About
                </Link>
              </li>
              <li
                class={`nav-item  ${
                  props.location.pathname === "/contact" ? "active" : ""
                }`}
              >
                <Link class="nav-link" to="/contact">
                  Contact
                </Link>
              </li>
            </ul>
          </div>
        </div>
      </nav>
    </div>
  );
}

export default withRouter(Navigation);
