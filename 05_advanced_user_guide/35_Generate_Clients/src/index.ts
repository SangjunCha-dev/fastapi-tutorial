import { DefaultService } from "./client";

async function main() {
    const response = DefaultService.createItemItemPost({
        name: "Plumbus",
        price: 5,
    });
    response.message
}

// ItemsService.createItemItemPost({"name": "Plumbus", price: 5})
// UsersServuce.createUserUserPost({})
