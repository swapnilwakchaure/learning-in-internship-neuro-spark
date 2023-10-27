import { useState } from "react";
import { Button } from "react-bootstrap";
import Accordion from "react-bootstrap/Accordion";

const FormBootStrap = () => {
  const [active, setActive] = useState("0");

  console.log('active: ',active);

  return (
    <div>
      <h1>React BootStrap Accordion</h1>

      <Button onClick={() => setActive(null)}>Toggle</Button>

      <Accordion activeKey={active} onSelect={(e) => setActive(e)}>
        <Accordion.Item eventKey="0">
          <Accordion.Header>
            <h3>Shipping Address</h3>
          </Accordion.Header>
          <Accordion.Body>
            <p>
              Lorem ipsum dolor sit amet consectetur, adipisicing elit. Corporis
              voluptatibus quasi dicta aliquid iusto rerum expedita id dolor
              dolorem doloribus fuga modi placeat, minima distinctio sint in
              rem, culpa consequatur!
            </p>
          </Accordion.Body>
        </Accordion.Item>
        <Accordion.Item eventKey="1">
          <Accordion.Header>
            <h3>Shipping Address</h3>
          </Accordion.Header>
          <Accordion.Body>
            <p>
              Lorem ipsum dolor sit amet consectetur, adipisicing elit. Corporis
              voluptatibus quasi dicta aliquid iusto rerum expedita id dolor
              dolorem doloribus fuga modi placeat, minima distinctio sint in
              rem, culpa consequatur!
            </p>
          </Accordion.Body>
        </Accordion.Item>
      </Accordion>
    </div>
  );
};

export default FormBootStrap;
