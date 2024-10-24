// import { createSlice, createAsyncThunk } from "@reduxjs/toolkit";
// import { server } from "../../api/api";

// const initialState = {
//   data: [],
//   status: "idle",
//   error: null,
// };

// const createSlices = (url, sliceName) => {
//   const fetchData = createAsyncThunk("fetchData", async () => {
//     const res = await server.get(url);
//     return res?.data;
//   });

//   const slice = createSlice({
//     sliceName,
//     initialState,
//     extraReducers: {
//       [fetchData.pending]: (state) => {
//         state.status = "loading";
//       },
//       [fetchData.fulfilled]: (state, action) => {
//         state.status = "succeeded";
//         state.data = action.payload;
//       },
//       [fetchData.rejected]: (state, action) => {
//         state.status = "failed";
//         state.error = action.error.message;
//       },
//     },
//   });

//   const selectAllData = (state) => state.data.data;

//   return {
//     slice.reducer,
//     selectAllData
//   };
// };

// export default createSlices;
