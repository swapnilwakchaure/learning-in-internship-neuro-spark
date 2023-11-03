import axios from "axios";
import { useState } from "react";
import { useForm } from "react-hook-form";
import styled from "styled-components";

const AddProductByForm = () => {
  const [category, setCategory] = useState('');

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmitProductForm = (data) => {
    if (data) {
      data.category = category;
      console.log('data: ',data);
      // axios
      //   .post("http://localhost:8080/users", data)
      //   .then((res) => {
      //     console.log("res: ", res.data);
      //   })
      //   .catch((error) => {
      //     console.log("error: ", error);
      //   });
    }
  };

  return (
    <div>
      <Header>Add Product Information</Header>

      <Form onSubmit={handleSubmit(onSubmitProductForm)}>
        <Box>
          <Label htmlFor="select category">Select Category</Label>
          <Select onChange={(e) => setCategory(e.target.value)}>
            <option value="">Select Category</option>
            <option value="Cities">Cities</option>
            <option value="Companies">Companies</option>
            <option value="Foods">Foods</option>
          </Select>
        </Box>
        <Box>
          <Label htmlFor="image_address">Image Address</Label>
          <Input
            type="url"
            className={`${errors.image_address ? "is-invalid" : ""}`}
            placeholder="Enter Image Address"
            {...register("image_address", {
              required: "Image Address is required",
              pattern: {
                value: /^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$/,
                message: "Please Enter Valid URL Address",
              },
            })}
          />
          {errors.image_address && <div>{errors.image_address.message}</div>}
        </Box>
        <Box>
          <Label htmlFor="youtube_link">Youtube Link</Label>
          <Input
            type="url"
            className={`${errors.youtube_link ? "is-invalid" : ""}`}
            placeholder="Enter youtube link address"
            {...register("youtube_link", {
              required: "youtube_link is required",
              pattern: {
                value: /^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$/,
                message: "Please Enter Valid URL Address",
              },
            })}
          />
          {errors.youtube_link && <div>{errors.youtube_link.message}</div>}
        </Box>
        <Box>
          <Label htmlFor="google_map">Google Map</Label>
          <Input
            type="url"
            className={`${errors.google_map ? "is-invalid" : ""}`}
            placeholder="Enter google map link"
            {...register("google_map", {
              required: "google map is required",
              pattern: {
                value: /^(https?|ftp):\/\/[^\s/$.?#].[^\s]*$/,
                message: "Please Enter Valid URL Address",
              },
            })}
          />
          {errors.google_map && <div>{errors.google_map.message}</div>}
        </Box>
        <Box>
          <Label htmlFor="address">Address</Label>
          <Input
            type="text"
            className={`${errors.address ? "is-invalid" : ""}`}
            placeholder="Enter Your Address"
            {...register("address", {
              required: "address is required",
              pattern: {
                value: /^[\w\s\-,.#'/\\]+$/,
                message: "Please Enter Valid URL Address",
              },
            })}
          />
          {errors.address && <div>{errors.address.message}</div>}
        </Box>
        <Box>
          <Label htmlFor="description">Description</Label>
          <Textarea
            type="text"
            className={`${errors.description ? "is-invalid" : ""}`}
            placeholder="write something about the place..."
            {...register("description", {
              required: "description is required",
              pattern: {
                value: /^[a-zA-Z0-9\s\n\.,!?'"-]*$/,
                message: "Please Enter Valid Description",
              },
            })}
          />
          {errors.description && <div>{errors.description.message}</div>}
        </Box>
        <Submit type="submit">ADD</Submit>
      </Form>
    </div>
  );
};

export default AddProductByForm;


const Header = styled.h1`
  width: 80%;
  max-width: 530px;
  margin: 20px auto;
  padding: 10px 0px;
  background: #1A237E;
  color: white;
`

const Form = styled.form`
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
  border-radius: 10px;
  width: 70%;
  max-width: 480px;
  margin: auto;
  padding: 20px 25px;
`

const Box = styled.div`
  margin-bottom: 10px;
  text-align: start;
  line-height: 25px;
`

const Label = styled.label`
  display: block;
  font-size: .95rem;
`

const Select = styled.select`
  width: 98%;
  padding: 10px;
  font-size: .95rem;

  &:focus {
    outline: none;  
    border-color: blue;
    transition: border-color 0.3s ease-in-out;
  }
`

const Input = styled.input`
  display: block;
  width: 95%;
  padding: 10px 0px 10px 10px;
  font-size: .95rem;

  &:focus {
    outline: none;  
    border-color: blue;
    transition: border-color 0.3s ease-in-out;
  }
`

const Textarea = styled.textarea`
  width: 95%;
  height: 100px;
  font-size: .95rem;
  padding: 10px 0px 10px 10px;

  &:focus {
    outline: none;  
    border-color: blue;
    transition: border-color 0.3s ease-in-out;
  }
`

const Submit = styled.button`
  width: 98%;
  display: block;
  padding: 10px 0px;
`