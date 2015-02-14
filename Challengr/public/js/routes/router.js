import { AppRouter } from 'marionette';

const AppRoutes = {
	'import': 'import',

    'register': 'register',
    'profile/:id(/)?': 'viewProfile',

    'profile/:id/create': 'createAi',

	'': 'defaultRoute'
};

// App Router
// ----------
export default AppRouter.extend({
	appRoutes: AppRoutes
});