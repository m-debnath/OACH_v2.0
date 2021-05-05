import React, { Component } from "react";
import axios from "axios";

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      departments: sessionData.oach_user_data.Department,
      primary_division: sessionData.primary_division,
      is_one_primary: sessionData.is_one_primary,
      selcted_division: sessionData.oach_user_data.Department[0].name,
    };
    this.getUserName = this.getUserName.bind(this);
    this.getDepartmentList = this.getDepartmentList.bind(this);
    this.getUserGreeting = this.getUserGreeting.bind(this);
    this.handleDepartmentChange = this.handleDepartmentChange.bind(this);
    this.handleDepartmentSubmit = this.handleDepartmentSubmit.bind(this);
  }
  
  getUserName() {
    let sessionDataObj = sessionData;
    let full_name = sessionDataObj.oach_user_data.first_name + " " + sessionDataObj.oach_user_data.last_name;
    return full_name;
  }
  
  getDepartmentList() {
    let optionItems = this.state.departments.map((item) =>
      <option key={item.name}>{item.name}</option>
    );
    return optionItems;
  }
  
  handleDepartmentChange(event) {
    this.setState({selcted_division: event.target.value});
    event.preventDefault();
  }
  
  handleDepartmentSubmit(event) {
    axios.post('', {
      selected_division: this.state.selcted_division
    })
    .then(function (response) {
      window.location.reload();
    })
    .catch(function(error) {
      window.location.reload();
    });
  }

  getUserGreeting() {
    let userGreeting = '';
    if (this.state.is_one_primary) {
      userGreeting = <span style={{fontSize: "16pt", color: "#000000", fontWeight: "bold", whiteSpace: "nowrap"}}>Your primary division is { this.state.primary_division }.</span>;
    } else {
      if (this.state.primary_division) {
        userGreeting = <span style={{fontSize: "16pt", color: "#000000", fontWeight: "bold", whiteSpace: "nowrap"}}>
          Your primary division is { this.state.primary_division }.
          <span style={{fontSize: "11pt", color: "#000000"}}> (You can change it below, if you wish so.) </span>
          </span>;
      } else {
        userGreeting = <span style={{fontSize: "16pt", color: "#000000", fontWeight: "bold", whiteSpace: "nowrap"}}>Please select division:</span>;
      }
    }
    return userGreeting;
  }
  
  render() {
    return (
      <div name="_swecontent" id="_swecontent" ot="_swecontent Frame">
        <div style={{height : '100%'}}>
          <div name="_svf0" id="_svf0" ot="View Frame" frameBorder="no" marginHeight="0" marginWidth="0" scrolling="auto" className="siebui-view">
            <div style={{height : '100%'}}>
              <table border="0" cellSpacing="0" cellPadding="1" width="50%">
                <tbody>
                  <tr>
                    <td>
                      <div id="s_S_A2_div" className="siebui-applet siebui-form siebui-collapsible-applet siebui-formapplet-column Selected siebui-active siebui-applet-active siebui-hilight" role="region" title="Select Division Form Applet" t2_hidden_applet="false">
                        <table datatable="0" summary="" cellSpacing="0" cellPadding="3" border="0">
                          <tbody>
                            <tr>
                              <td valign="middle" colSpan="2" rowSpan="1">
                                <div className="mceGridField siebui-value mceField">
                                  <span id="s_2_1_5_0" name="s_2_1_5_0" className="siebui-ctrl-text siebui-input-align-left">
                                    &nbsp;
                                    <label id="s_2_1_5_0_Label">
                                      { this.getUserGreeting() }
                                    </label>
                                  </span>
                                </div>
                              </td>
                            </tr>
                          </tbody>
                        </table>
                        <table datatable="0" summary="" cellSpacing="0" cellPadding="0" border="0">
                          <tbody>
                            <tr>
                              <td>&nbsp;</td>
                            </tr>
                          </tbody>
                        </table>
                        <table datatable="0" summary="" cellSpacing="0" cellPadding="3" border="0">
                          <tbody>
                            <tr>
                              <td style={{height: "24px"}}></td>
                              <td nowrap="" valign="middle" colSpan="2" rowSpan="1">
                                <div className="mceGridLabel siebui-label mceLabel" align="Right">
                                  &nbsp;<span id="Division_Label">Division:</span>
                                </div>
                              </td>
                              <td nowrap="" valign="middle" colSpan="2" rowSpan="1">
                                <div className="mceGridField siebui-value mceField">
                                  <span role="status" aria-live="polite" className="ui-helper-hidden-accessible"></span>
                                  <select onChange={this.handleDepartmentChange} defaultValue={ this.state.primary_division ? this.state.primary_division : this.state.selected_division} name="s_2_1_8_0" aria-labelledby="Division_Label" aria-label="Division" style={{height: "24px", width: "270px"}} className="siebui-ctrl-select siebui-input-popup siebui-align-left siebui-input-align-left ui-autocomplete-input" disabled={this.state.is_one_primary}>
                                  { this.getDepartmentList() }
                                  </select>
                                  <span id="s_2_1_8_0_span" style={{display: "none"}}></span>
                                </div>
                              </td>
                              <td rowSpan="2" colSpan="2"></td>
                              <td rowSpan="2" colSpan="3"></td>
                              <td rowSpan="2" colSpan="1"></td>
                            </tr>
                          </tbody>
                        </table>
                        <table datatable="0" summary="" cellSpacing="0" cellPadding="3" border="0">
                          <tbody>
                            <tr>
                              <td style={{height: "24px"}}></td>
                              <td rowSpan="1" colSpan="2"></td>
                              <td nowrap="" valign="middle" colSpan="2" rowSpan="1">
                                <div className="mceGridField siebui-value mceField">
                                  <button onClick={this.handleDepartmentSubmit} type="button" style={{marginLeft: "55px"}} className="siebui-ctrl-btn siebui-icon-t2divselect s_2_1_4_0" id="s_2_1_4_0_Ctrl" name="s_2_1_4_0" data-display="Select" title="Select Division:Select" aria-label="Select Division:Select" data-seq="0" disabled={this.state.is_one_primary}>
                                    <span>Select</span>
                                  </button>
                                </div>
                              </td>
                              <td rowSpan="2" colSpan="2"></td>
                              <td rowSpan="2" colSpan="3"></td>
                              <td rowSpan="2" colSpan="1"></td>
                            </tr>
                          </tbody>
                        </table>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
      );
    }
  }
  