import { AppRouter } from 'marionette';

const AppRoutes = {
	'import': 'import',
	'': 'defaultRoute'

};

// App Router
// ----------
export default AppRouter.extend({
	appRoutes: AppRoutes
});