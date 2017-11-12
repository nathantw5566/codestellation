class Indecision extends React.Component {
  // update() {
  //   this.setState(console.log("aaaa"));
  //   console.log("aaaa");
  //   var random = Math.floor(Math.random() * 8);
  //   img[random] = "../images/1.jpg";
  // }
  // componentDidMount = function() {
  //   this.interval = setInterval(this.update, 1000);
  // };
  // componentWillUnmount = function() {
  //   clearInterval(this.interval);
  // };
  render() {
    const title = "Indecision";
    const subtitle = "Put your life";
    const options = ["One", "Two", "Three"];

    const img = [
      "../images/smile.jpg",
      "../images/smile2.jpg",
      "../images/smile3.jpg",
      "../images/smile4.jpg",
      "../images/smile5.jpg",
      "../images/smile6.jpg",
      "../images/smile.jpg",
      "../images/smile2.jpg",
      "../images/smile3.jpg"
    ];
    var random = Math.floor(Math.random() * 8);
    img[random] = "../images/1.jpg";
    return (
      <div>
        {/*<Header title={title} subtitle={subtitle} />*/}
        <Image images={img.slice(0, 3)} />
        <Image images={img.slice(3, 6)} />
        <Image images={img.slice(6, 10)} />
        <Action />
        <Options options={options} />
        <AddOption />
      </div>
    );
  }
}

class Image extends React.Component {
  render() {
    var imgStyle = {
      height: 100,
      width: 100
    };
    return (
      <div>
        {this.props.images.map(dir => {
          return <img key={dir} style={imgStyle} src={dir} />;
        })}
      </div>
    );
  }
}

class Action extends React.Component {
  render() {
    return (
      <div>
        <button>What Should I do?</button>
      </div>
    );
  }
}

class Options extends React.Component {
  handleRemoveAll() {
    alert("Handle remove all");
  }
  render() {
    return (
      <div>
        <button onClick={this.handleRemoveAll}>Remove All</button>
        <p>{this.props.options.length}</p>
        {this.props.options.map(option => {
          return <Option key={option} optionText={option} />;
        })}
      </div>
    );
  }
}

class Option extends React.Component {
  render() {
    console.log(this.props);
    return <div>{this.props.optionText}</div>;
  }
}

class AddOption extends React.Component {
  handleAddOption() {
    e.preventDefault();

    const option = e.target.elements.option.value.trim();
    if (option) {
      alert(option);
    }
  }
  render() {
    return (
      <div>
        <form onSubmit={this.handleAddOption}>
          <input type="text" name="option" />
          <button>Add Option</button>
        </form>
      </div>
    );
  }
}

ReactDOM.render(<Indecision />, document.getElementById("app"));
setInterval(()=>{
  ReactDOM.render(<Indecision />, document.getElementById("app"));
},2000);