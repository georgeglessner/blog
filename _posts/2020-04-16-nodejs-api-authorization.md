---
layout: post
title:  "API Bearer Token Authorization with Node.js"
tags: node, API, authentication, security, javascript
---

API authorization should be a must-have for most public-facing APIs. There are other ways to implement authorization suchs as JWTs, but I am going to show you how to implement bearer token authentication in a Node.js API. 

The first thing you will need to do is install two packages from npm, `passport` and `passport-http-bearer`.

```
npm i passport passport-http-bearer
```

The following code all happens inside the `app.js` file. 

Import your packages.

```javascript
const passport = require("passport");
const BearerStrategy = require("passport-http-bearer");
```

Now that we have the packages imported, the next part of the implementation is checking to make sure the bearer token passed over is valid. We do this by using the bearer starategy that we imported as well as creating an authentication function that will utilize that bearer strategy. 

The bearer strategy is implemented below. The token will be passed in from the authentication function we will write in the next step. A detailed explanation of the bearery strategy can be found in the docs [here](http://www.passportjs.org/packages/passport-http-bearer/#usage).
```javascript
passport.use(
	new BearerStrategy(function(token, done) {
		// Implement your token checking logic here
		// Most likely a call to a database 
		if(VALID TOKEN){
			return done(null, true);
		} else{
			return done(null, false);
		}
	})
);
```

The next thing you will want to do is create the authentication function. This is not required, I just think it makes everything cleaner. More information on passport authentication can be found [here](http://www.passportjs.org/docs/#authenticate).

> By default, if authentication fails, Passport will respond with a 401 Unauthorized status, and any additional route handlers will not be invoked. If authentication succeeds, the next handler will be invoked.

```javascript
function authentication() {
	return passport.authenticate("bearer", { session: false});
}
````

Finally, to tie everything together and make all your API endpoints require authorization, configure your app to use the authentication function.

```javascript
app.use(authentication());
```

If you only want to invoke the authorization on certain endpoints, do not make your app use `authentication()` but instead use the authentication function in your route as follows.

```javascript
app.use("/route", authentication(), some_function);
```

And that's it, you should now be able to authenticate API requests by the bearer token passed through in the authorization header. 