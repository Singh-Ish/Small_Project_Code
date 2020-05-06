import React from 'react';
import axios from "axios";



class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      users: [],
      name: "",
      email: "",
      role: "",
      id:0
    };
  }

  componentDidMount() {
    axios.get("http://127.0.0.1:5000/user").then((res) => {
      this.setState({
        users: res.data,
        name: "",
        email: "",
        role: "",
        id:0
      });
      console.log(res)
    });
  }

  namechange = (event) => {
    this.setState({
      name: event.target.value,
    })
  }

  emailchange = (event) => {
    this.setState({
      email: event.target.value,
    })
  }

  rolechange = (event) => {
    this.setState({
      role: event.target.value,
    })
  }

  submit(e,id){


  }

  render() {
    return (
      <div className="App container mt-5">
        <h1> Hello from App.js</h1>

        <div className="row mt-5">
          <div className="col lg-6 mt-5">
            <form
              onSubmit={(e) => {
                this.submit(e,this.state.id);
              }}
            >
              <div className="form=group">
                <input
                  type="text"
                  onChange={(e) => {
                    this.namechange(e);
                  }}
                  className="from-control"
                  placeholder=" Full Name"
                ></input>
              </div>
              <br></br>

              <div className="form=group">
                <input
                  type="email"
                  onChange={(e) => {
                    this.emailchange(e);
                  }}
                  className="from-control"
                  placeholder="Please write your Email"
                ></input>
              </div>
              <br></br>
              <div className="form=group">
                <input
                  type="text"
                  onChange={(e) => {
                    this.rolechange(e);
                  }}
                  className="from-control"
                  placeholder="Access Role "
                ></input>
              </div>
              <br></br>

              <button className="btn btn-block btn-primary"> Submit</button>
            </form>
          </div>
          <div className="col lg-6 mt-5">
            <h3> Users </h3>
            <table className="table" id="book-table">
              <thead>
                <tr>
                  <th>Name </th>
                  <th>Email</th>
                  <th>Role</th>
                  <th>Edit </th>
                  <th> Delete</th>
                </tr>
              </thead>
              <tbody>
                {this.state.users.map((user) => (
                  <tr>
                    <td>{user.name}</td>
                    <td>{user.email}</td>
                    <td>{user.role}</td>
                    <td>
                      <button className="btn btn-warning">
                        <span class="material-icons">edit</span>
                      </button>
                    </td>
                    <td>
                      <button className="btn btn-danger">
                        <span class="material-icons">delete</span>
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    );
  }
}

export default App;
