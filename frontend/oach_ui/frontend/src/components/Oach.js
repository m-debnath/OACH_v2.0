import React, { Component } from "react";
import { v4 as uuidv4 } from "uuid";
import axios from "axios";
import OachAccount from "./OachAccount";
import OachProduct from "./OachProduct";
import OachOrder from "./OachOrder";
import OachInvoice from "./OachInvoice";

export default class Oach extends Component {
  constructor(props) {
    super(props);
    this.state = {
      departments: sessionData.oach_user_data.Department,
      primary_division: sessionData.primary_division,
      is_one_primary: sessionData.is_one_primary,
      selcted_division: sessionData.oach_user_data.Department[0].name,
      search_account_url: sessionData.search_account_trans_params.RequestURL,
      search_account_auth: sessionData.search_account_trans_params.Authorization,
    };
    this.handleSearchChange = this.handleSearchChange.bind(this);
    this.handleSearchSubmit = this.handleSearchSubmit.bind(this);
  }

  handleSearchChange(event) {
    this.setState({search_account_number: event.target.value});
    event.preventDefault();
  }
  
  handleSearchSubmit(event) {
    let oach = this;
    if (this.state.search_account_url && this.state.search_account_number) {
      let search_account_url = this.state.search_account_url.replace("<AccountNumber>", this.state.search_account_number).replace("<Locale>", "LVI");
      let search_account_auth = this.state.search_account_auth;
      let search_account_hdr_value = uuidv4().replaceAll("-", "");
      axios.get(search_account_url, {
        headers: {
          "Authorization": search_account_auth,
          "X-Oach-Request-Id": search_account_hdr_value
        }
      })
      .then(function (response) {
        if (response.status === 200) {
          oach.setState({
            oach_account_id: response.data.id,
            oach_request_id: search_account_hdr_value,
          });
        }
      })
      .catch(function(error) {
        console.error(error);
      });
    }
  }

  static getDerivedStateFromProps(nextProps, prevState) {
    if (nextProps.oach_account_id !== prevState.oach_account_id && nextProps.oach_account_id !== undefined) {
        return {
            oach_account_id: nextProps.oach_account_id,
            oach_request_id: nextProps.oach_request_id
        };
    }
    return prevState;
  }
  
  render() {
    return (
      <div name="_swecontent" id="_swecontent" ot="_swecontent Frame">
        <div style={{height : '100%'}}>
            <div name="_svf0" id="_svf0" ot="View Frame" frameBorder="no" marginHeight="0" marginWidth="0" scrolling="Yes" className="siebui-view" style={{overflowX: "hidden", overflowY: "auto", maxHeight: "100%"}}>
                <div style={{height : '100%'}}>
                    <table border="0" cellSpacing="0" cellPadding="1" width="100%">
                        <tbody>
                            <tr>
                              <td>
                                  <div id="s_S_A2_div" className="siebui-applet siebui-form siebui-collapsible-applet siebui-formapplet-column Selected siebui-active siebui-applet-active siebui-hilight" role="region" title="Select Division Form Applet" t2_hidden_applet="false">
                                      <table datatable="0" summary="" cellSpacing="0" cellPadding="3" border="0">
                                          <tbody>
                                              <tr>
                                                  <td nowrap="" valign="middle" colSpan="2" rowSpan="1">
                                                      <div className="mceGridLabel siebui-label mceLabel" align="Right">
                                                          &nbsp;<span id="Division_Label">Account #:</span>
                                                      </div>
                                                  </td>
                                                  <td nowrap="" valign="middle" colSpan="2" rowSpan="1">
                                                      <div className="mceGridField siebui-value mceField">
                                                          <input onChange={this.handleSearchChange} type="text" name="search_account_number" aria-labelledby="Account_Number_Label" aria-label="Account #" style={{height: "24px", width: "200px"}} className="siebui-ctrl-input siebui-align-left siebui-input-align-left s_2_1_3_0" maxLength="30" tabIndex="0" ></input>
                                                      </div>
                                                  </td>
                                                  <td nowrap="" valign="middle" colSpan="2" rowSpan="1">
                                                      <div className="mceGridField siebui-value mceField">
                                                          <button onClick={this.handleSearchSubmit} type="button" className="siebui-ctrl-btn siebui-icon-t2divselect s_2_1_4_0" id="s_2_1_4_0_Ctrl" name="s_2_1_4_0" data-display="Search" title="Search Customer:Search" aria-label="Search Customer:Search" data-seq="0">
                                                          <span>Search</span>
                                                          </button>
                                                      </div>
                                                  </td>
                                              </tr>
                                          </tbody>
                                      </table>
                                  </div>
                              </td>
                            </tr>
                        </tbody>
                    </table>
                    <div className="t2_oach_container">
                      <div id="S_A1" applet_name="T2 OACH Applet">
                          <a id="SWETopHidden1" aria-hidden="true" tabIndex="-1"></a>
                          <a name="SWEApplet1" id="SWEApplet1" className="next-item-applet" href="#SWEApplet1" title="Account" tabIndex="-1" aria-hidden="true" role="heading"></a>
                          <div id="s_S_A1_div" className="siebui-applet siebui-form siebui-collapsible-applet siebui-formapplet-column Selected siebui-applet-active siebui-hilight" role="region" title="Account Form Applet" tabIndex="0" scrolling="Yes">
                              <span id="1_c_err" style={{display: "none"}}>
                                  <span id="1_err"></span>
                              </span>
                              <div id="t2_oach_main" title="">
                                <div className="t2_oach_left">
                                    <div className="t2_oach_left_inner">
                                        <OachAccount 
                                            oach_account_id={this.state.oach_account_id}
                                            oach_request_id={this.state.oach_request_id}
                                        />
                                        <OachProduct 
                                            oach_account_id={this.state.oach_account_id}
                                            oach_request_id={this.state.oach_request_id}
                                        />
                                        <OachOrder 
                                            oach_account_id={this.state.oach_account_id}
                                            oach_request_id={this.state.oach_request_id}
                                        />
                                        <OachInvoice 
                                            oach_account_id={this.state.oach_account_id}
                                            oach_request_id={this.state.oach_request_id}
                                        />
                                    </div>
                                </div>
                              </div>
                          </div>
                      </div>
				          </div>
                </div>
            </div>
        </div>
      </div>
      );
    }
  }
  