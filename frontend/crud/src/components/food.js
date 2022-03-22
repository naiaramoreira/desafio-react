import React, { Component} from 'react';

class Food extends Component {

  state = {
    food: []
  }

  loadFood = () => {
    fetch('http://127.0.0.1:8000/api/food/', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Token ${this.props.token}`
      },
      body: JSON.stringify(this.state.credentials)
    })
    .then( data => data.json())
    .then(
      data => {
        this.setState({food: data})
      }
    )
    .catch( error => console.error(error))
  }

  render() {
    return (
        <div>
          <table>
            <thead>
              <tr>
                <th>Alimento</th>
                <th>Proteinas</th>
                <th>Carboidratos</th>
                <th>Gordura</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                 { this.state.food.map( food => {
                  return <td> food </td>
                })}
              </tr>
            </tbody>
          </table>
        </div>
    );
    }
  }

export default Food;

