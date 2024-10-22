import * as React from "react";
import AppBar from "@mui/material/AppBar";
import Box from "@mui/material/Box";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import Avatar from "@mui/material/Avatar";
import Button from "@mui/material/Button";
import noam from "../pics/noam.jpg";

const img =
  "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkQ5lHZ2gidoAutn4qXnrgtuG_2OVX9CCd1X9EVUXN-UPwjE3PSw0-RHEp4kZuaJ9ZcnI&usqp=CAU";

export const Navbar = () => {
  return (
    <AppBar position="static" style={{ backgroundColor: "#840000" }}>
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <Button href={noam}>
            <Avatar
              sx={{ display: { xs: "none", md: "flex" }, mr: 3 }}
              src={noam}
            />
          </Button>
          <Typography
            variant="h6"
            noWrap
            component="a"
            href="/"
            sx={{
              mr: 2,
              display: { xs: "none", md: "flex" },
              fontFamily: "monospace",
              fontWeight: 700,
              letterSpacing: ".3rem",
              color: "inherit",
              textDecoration: "none",
            }}
          >
            Hey Noam
          </Typography>

          <Box sx={{ flexGrow: 1, display: { xs: "none", md: "flex" } }}>
            {true && (
              <Button
                sx={{ my: 2, color: "white", display: "block" }}
                href={img}
              >
                אמור להיות כפתור חזור אבל באסה
              </Button>
            )}
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
};
