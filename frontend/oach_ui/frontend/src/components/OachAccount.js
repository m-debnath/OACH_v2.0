import React, { Component } from "react";
import axios from "axios";
import { makeStyles } from '@material-ui/core/styles';
import Tooltip from "@material-ui/core/Tooltip";

const useStylesOach = makeStyles((theme) => ({
    arrow: {
        color: theme.palette.common.black,
    },
    tooltip: {
        fontFamily: "Tele2 Slab Web Bold",
        fontSize: "14px",
        color: "#fff",
        maxWidth: "400px",
        alignSelf: "center",
        textShadow: "none",
        textAlign: "center",
        backgroundColor: theme.palette.common.black,
    },
}));

function OachAccountIndicatorTooltip(props) {
    const classes = useStylesOach();  
    return <Tooltip arrow classes={classes} {...props} interactive />;
}

export default class OachAccount extends Component {
  constructor(props) {
    super(props);
    this.state = {
        account_hier_url: sessionData.account_hier_trans_params.RequestURL,
        account_hier_auth: sessionData.account_hier_trans_params.Authorization,
        oach_account_id: props.oach_account_id,
        oach_request_id: props.oach_request_id,
        menu_open: false,
    };
    this.openMenuDetails = this.openMenuDetails.bind(this);
  }

  static getDerivedStateFromProps(nextProps, prevState) {
    if (nextProps.oach_account_id !== prevState.oach_account_id) {
        return {
            oach_account_id: nextProps.oach_account_id,
            oach_request_id: nextProps.oach_request_id
        };
    }
    return prevState;
  }

  componentDidUpdate(prevProps, prevState) {
    let customerAccountNumber = "";
    let customerAccountName = "";
    let billingAccountNumber = "";
    let accountType = "";
    let accountTypeClass = "";
    let accountSubType = "";
    let accountStatus = "";
    let accountStatusClass = "";
    let accountStanding = "";
    let accountStandingClass = "";
    let accountProactivityCount = "2";
    let accountSSNLabel = "SSN";
    let accountSSN = "";
    let accountContactName = "";
    let accountContactMobile = "";
    let accountContactEmail = "";
    let accountAddressLine1 = "";
    let accountAddressLine2 = "";
    let accountAddressLine3 = "";
    let accountCreditLimit = "";
    let a = this;
    if (this.state.oach_account_id && this.state.account_hier_url && prevState.oach_account_id !== this.state.oach_account_id) {
        let account_hier_url = this.state.account_hier_url.replace("<CustomerAccountId>", this.state.oach_account_id).replace("<Locale>", "LVI");
        axios.get(account_hier_url, {
          headers: {
            "Authorization": this.state.account_hier_auth,
            "X-Oach-Request-Id": this.state.oach_request_id
          }
        })
        .then(function (response) {
          if (response.status === 200) {
            customerAccountNumber = response.data.AccountNumber;
            customerAccountName = response.data.AccountName;
            for (let childAccount of response.data.children) {
                if (childAccount.AccountClass === "Billing") {
                    billingAccountNumber = childAccount.AccountNumber;
                }
            }
            accountType = response.data.AccountType;
            accountTypeClass = response.data.AccountType.toLowerCase();
            accountSubType = response.data.AccountSubType;
            accountStatus = response.data.AccountStatus;
            accountStatusClass = response.data.AccountStatus.toLowerCase();
            accountStanding = response.data.AccountStanding;
            accountStandingClass = response.data.AccountStanding.toLowerCase().replaceAll(" ", "-");
            accountSSN = response.data.AccountSSN;
            if (accountType === "Business") {
                accountSSNLabel = "Org #";
            }
            accountContactName = response.data.AccountName;
            accountContactEmail = response.data.AccountEmailAddress;
            accountContactMobile = response.data.AccountMobile;
            accountAddressLine1 = response.data.AccountAddress.split(",")[0];
            accountAddressLine2 = response.data.AccountAddress.split(",")[1];
            accountAddressLine3 = response.data.AccountAddress.split(",")[2];
            accountCreditLimit = response.data.AccountCreditLimit;
            a.setState({
                customerAccountNumber: customerAccountNumber,
                customerAccountName: customerAccountName,
                billingAccountNumber: billingAccountNumber,
                accountType: accountType,
                accountTypeClass: accountTypeClass,
                accountSubType: accountSubType,
                accountStatus: accountStatus,
                accountStatusClass: accountStatusClass,
                accountStanding: accountStanding,
                accountStandingClass: accountStandingClass,
                accountSSN: accountSSN,
                accountSSNLabel: accountSSNLabel,
                accountContactName: accountContactName,
                accountContactEmail: accountContactEmail,
                accountContactMobile: accountContactMobile,
                accountAddressLine1: accountAddressLine1,
                accountAddressLine2: accountAddressLine2,
                accountAddressLine3: accountAddressLine3,
                accountCreditLimit: accountCreditLimit,
                accountProactivityCount: accountProactivityCount,
            });
          }
        })
        .catch(function(error) {
          console.error(error);
        });
    }
  }

  openMenuDetails() {
    const currentState = this.state.menu_open;
    this.setState({ menu_open: !currentState });
  }

  renderComponent() {
      if (this.state.oach_account_id) {
          return (
            <div id="t2-accform-applet" applet_name="oach_account_form">
                <div className="header">
                    <div className="left">
                        <div tip-id="" className="title">{ this.state.customerAccountName }</div>
                        <div className="details">
                            <div>
                                <div className="t2-acc-fltr-title">
                                    <div className="t2-acc-fltr-title-text customer disabled current">
                                        <span className="t2-acc-fltr-field acc-className blue">Customer</span> 
                                        <span className="t2-acc-fltr-divider blue">-</span> 
                                        <span data-label="Customer" className="t2-acc-fltr-field acc-nr">{ this.state.customerAccountNumber }</span>
                                    </div> 
                                    <div className="t2-acc-fltr-title-text billing">
                                        <span className="t2-acc-fltr-field acc-className blue">Billing</span> 
                                        <span className="t2-acc-fltr-divider blue">-</span> 
                                        <span data-label="Billing" className="t2-acc-fltr-field acc-nr">{ this.state.billingAccountNumber }</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div> 
                    <div className="center">
                        <div className="acc-indicators">
                            <OachAccountIndicatorTooltip title={
                                 <div className="indicator-tooltip" style={{padding: "10px"}}>
                                    <div className="row">
                                        <span className="label">Account type</span>: { this.state.accountType }
                                    </div> 
                                    <div className="row">
                                        <span className="label">Account sub type</span>: { this.state.accountSubType }
                                    </div>
                                </div>
                            }>
                                <span data-label="Account type" data-value="Residential" tip_id="1" className={ `indicator blue type ${this.state.accountTypeClass}` }></span>
                            </OachAccountIndicatorTooltip>
                            <OachAccountIndicatorTooltip title={
                                <div className="indicator-tooltip" style={{padding: "10px"}}>
                                    <div className="row">
                                        <span className="label">Status</span>: { this.state.accountStatus }
                                    </div>
                                </div>
                            }>
                                <span data-label="Status" data-value="Active" tip_id="2" className={ `indicator blue status ${this.state.accountStatusClass}` }></span>
                            </OachAccountIndicatorTooltip>
                            <OachAccountIndicatorTooltip title={
                                <div className="indicator-tooltip" style={{padding: "10px"}}>
                                    <span className="label">{ this.state.accountStanding }</span>
                                </div>
                            }>
                                <span data-label={ this.state.accountStanding } tip_id="3" className={ `indicator blue ${this.state.accountStandingClass}` }></span>
                            </OachAccountIndicatorTooltip>
                        </div>
                    </div>
                    <div className="right">
                        <div id="t2_proact_bell" className="proact-bell" style={{color: `rgb(204, 0, 51)`}}>
                            <span className="proact-count">{ this.state.accountProactivityCount }</span>
                        </div> 
                        <div className="menu-container">
                            <div className="menu">
                                <div className="menu-actions" onClick={this.openMenuDetails}></div>
                                <div className={ `item-container ${this.state.menu_open ? 'open': null}` }>
                                    <div className="menu-item">Update contact</div>
                                    <div className="menu-item">Update address</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div> 
                <div className="body">
                    <div className="main">
                        <div className="panel main-left">
                            <div className="field"><span className="label">{ this.state.accountSSNLabel }:</span>
                                <span data-label="SSN">{ this.state.accountSSN }</span>
                            </div>
                            <div className="field">
                                <div className="panel left">
                                    <span className="label ident">Contact:</span>
                                    <div style={{display: "flex", flexDirection: "column"}}>
                                        <div title="Open Contact Overview" className="contacts icon-box">
                                            <i className="fa fa-address-book-o"></i>
                                        </div>
                                    </div>
                                </div>
                                <div className="panel right">
                                    <div className="field-row">
                                        <span data-label="Contact" className="row nolink">{ this.state.accountContactName }</span>
                                    </div>
                                    <span data-label="Mobile Phone #" className="row">{ this.state.accountContactMobile }</span>
                                    <span data-label="Email" className="row">{ this.state.accountContactEmail }</span>
                                </div>
                            </div>
                            <div className="field">
                                <div className="panel left">
                                    <span className="label ident">Address:</span>
                                    <div style={{display: "flex", flexDirection: "column"}}>
                                        <div title="View on Map/Open Address Overview" className="address icon-box">
                                            <i className="fa fa-map-marker"></i>
                                        </div>
                                    </div>
                                </div>
                                <div className="panel right">
                                    <span data-label="Address" className="row">{ this.state.accountAddressLine1 }</span>
                                    <span data-label="address_line_2" className="row">{ this.state.accountAddressLine2 }</span>
                                    <span data-label="address_line_3" className="row">{ this.state.accountAddressLine3 }</span>
                                </div>
                            </div>
                        </div>
                        <div className="panel main-right">
                            <div className="field">
                                <span className="label">Customer Credit Limit:</span>
                                <span data-label="Customer Credit Limit">{ this.state.accountCreditLimit }</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
          );
      } else {
          return <div style={{display: "none"}}></div>
      }
  }

  render() {
    return (
      this.renderComponent()
      );
    }
  }
  